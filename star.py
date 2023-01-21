import json

import requests


def get_star_remind():
	url = "https://v2.alapi.cn/api/star"
	token = "3bLV8mCneLv95SHo"
	star = "virgo"
	payload = f"token={token}&star={star}"
	headers = {'Content-Type': "application/x-www-form-urlencoded"}
	response = requests.request("POST", url, data=payload, headers=headers)
	data = json.loads(response.content)["data"]["day"]

	she_star = "处女座"
	daily_fortune = data["all_text"].replace("星^座^屋", "")
	love_index = data["love"]
	lucky_color = data["lucky_color"]
	return lucky_color, she_star, love_index, daily_fortune

