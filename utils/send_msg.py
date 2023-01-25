from datetime import datetime, date
from time import localtime

from requests import post

from config.config import config
from utils.birthday import get_birthday
from utils.color import get_color
from utils.log import log_info


def send_message(to_user: str, params: dict):
	"""
	发送消息
	Args:
		to_user: 微信ID
		params: 参数
			{
				access_token: "", # 微信公共平台access_token
				weather: {
							region: "", # 所在地区
							weather: "", # 天气
							temp: "", # 温度
							wind_dir: "", # 风向
						},  # 天气
				star: {
							lucky_color: "", # 幸运颜色
							she_star: "", # 对方的星座
							love_index: "", # 爱情指数
							daily_fortune: "", # 每日运势
						}# 星座
			}

	Returns:

	"""
	url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(params["access_token"])
	week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
	year = localtime().tm_year
	month = localtime().tm_mon
	day = localtime().tm_mday
	today = datetime.date(datetime(year=year, month=month, day=day))
	week = week_list[today.isoweekday() % 7]
	# 获取在一起的日子的日期格式
	love_year = int(config.birthday.love_date.split("-")[0])
	love_month = int(config.birthday.love_date.split("-")[1])
	love_day = int(config.birthday.love_date.split("-")[2])
	love_date = date(love_year, love_month, love_day)
	# 获取在一起的日期差
	love_days = str(today.__sub__(love_date)).split(" ")[0]
	# 获取所有生日数据
	birthdays = {}
	birthdays.update({"she_birthday": config.birthday.she_birthday})
	birthdays.update({"my_birthday": config.birthday.my_birthday})
	weather = params["weather"]
	star = params["star"]
	print("to_user: ", to_user)
	data = {
		"touser": to_user,
		"template_id": config.wechat.template_id,
		"url": "http://weixin.qq.com/download",
		"topcolor": "#FF0000",
		"data": {
			"date": {
				"value": "{} {}".format(today, week),
				"color": get_color()
			},
			"region": {
				"value": weather["region"],
				"color": get_color()
			},
			"weather": {
				"value": weather["weather"],
				"color": get_color()
			},
			"temp": {
				"value": weather["temp"],
				"color": get_color()
			},
			"wind_dir": {
				"value": weather["wind_dir"],
				"color": get_color()
			},
			"love_day": {
				"value": love_days,
				"color": get_color()
			},
			"lucky_color": {
				"value": star["lucky_color"],
				"color": get_color()
			},
			"she_star": {
				"value": star["she_star"],
				"color": get_color()
			},
			"love_index": {
				"value": star["love_index"],
				"color": get_color()
			},
			"daily_fortune": {
				"value": star["daily_fortune"],
				"color": get_color()
			}

		}
	}
	for key, value in birthdays.items():
		# 获取距离下次生日的时间
		birth_day = get_birthday(value["birthday"], year, today)
		if birth_day == 0:
			birthday_data = f"今天{value['name']}生日哦，祝{value['name']}生日快乐！"
		else:
			birthday_data = f"距离{value['name']}的生日还有{birth_day}天"
		# 将生日数据插入data
		data["data"][key] = {"value": birthday_data, "color": get_color()}
	headers = {
		'Content-Type': 'application/json',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
		              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
	}
	response = post(url, headers=headers, json=data).json()
	if response["errcode"] == 40037:
		log_info.error("推送消息失败，请检查模板id是否正确")
	elif response["errcode"] == 40036:
		log_info.error("推送消息失败，请检查模板id是否为空")
	elif response["errcode"] == 40003:
		log_info.error("推送消息失败，请检查微信号是否正确")
	elif response["errcode"] == 0:
		log_info.info("推送消息成功")
	else:
		log_info.error("msg send failed: ", response)
