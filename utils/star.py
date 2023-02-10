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
	# {'ji': '晚上喝太多水', 'yi': '发展副业计划', 'all': '85%', 'date': '3 / 2月', 'love': '88%', 'work': '75%', 'money': '71%',
	#  'health': '80%', 'notice': '保留自我的个性', 'discuss': '77%',
	#  'all_text': '整体运势平平稳稳，能做自己喜欢做的事。相比起合群，你会注重保留自己的个性，即便想法或是计划得不到支持，也不会轻易就放弃。生活方面思想趋于成熟，懂得换位思考，但也容易受感情牵绊。星5座5屋',
	#  'love_text': '单身的或能打破暧昧确定恋爱关系。恋爱中的沉浸在甜蜜的二人世界中，感情急速升温。', 'work_text': '在大脑酝酿的新想法，还没有落实的机会，要不然就是一开始就容易碰壁。',
	#  'lucky_star': '天秤座', 'money_text': '建议考虑开拓副业计划，稳守现状很难实现财富自由，也要多学习理财之道。',
	#  'health_text': '保持多喝水的习惯，但不要在睡前喝太多水，半夜起来频繁上厕所也会影响休息。', 'lucky_color': '青', 'lucky_number': '3'}
	return {
		"lucky_color": lucky_color,
		"she_star": she_star,
		"love_index": love_index,
		"daily_fortune": daily_fortune,
	}
