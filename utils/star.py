import json

import requests


def get_star_remind() -> dict:
	"""
	获取星座提醒信息
	day.ji	忌
	day.yi	宜
	day.notice	本日提醒
	day.date	更新日期
	day.all	综合运势
	day.all_text	综合运势说明
	day.love	爱情指数
	day.love_text	爱情指数说明
	day.work	事业学业指数
	day.work_text	事业学业指数说明
	day.health	健康指数
	day.health_text	健康指数说明
	day.discuss	商谈指数
	day.money	财富指数
	day.money_text	财富指数说明
	day.lucky_star	幸运星座
	day.lucky_color	幸运颜色
	day.lucky_number	幸运数字
	week.lucky_star	本周幸运星座
	week.take_star	本周提防星座
	Returns:

	"""
	url = "https://v2.alapi.cn/api/star"
	token = "3bLV8mCneLv95SHo"
	star = "virgo"
	payload = f"token={token}&star={star}"
	headers = {'Content-Type': "application/x-www-form-urlencoded"}
	response = requests.request("POST", url, data=payload, headers=headers)
	data = json.loads(response.content)["data"]["day"]

	she_star = "处女座"
	daily_fortune = data["all_text"]
	love_index = data["love"]
	lucky_color = data["lucky_color"]
	return {
		"lucky_color": lucky_color,
		"she_star": she_star,
		"love_index": love_index,
		"daily_fortune": daily_fortune,
	}
