import os
import sys

from requests import get

from config.config import config
from utils.log import log_info


def get_weather() -> dict:
	"""
	获取天气信息

	Returns:

	"""
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
		              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
	}
	key = config.weather.weather_key
	region = config.weather.region
	region_url = f"https://geoapi.qweather.com/v2/city/lookup?location={region}&key={key}"
	response = get(region_url, headers=headers).json()
	if response["code"] == "404":
		log_info.error("推送消息失败，请检查地区名是否有误！")
		os.system("pause")
		sys.exit(1)
	elif response["code"] == "401":
		log_info.error("推送消息失败，请检查和风天气key是否正确！")
		os.system("pause")
		sys.exit(1)
	else:
		# 获取地区的location--id
		location_id = response["location"][0]["id"]
	weather_url = f"https://devapi.qweather.com/v7/weather/now?location={location_id}&key={key}"
	response = get(weather_url, headers=headers).json()
	# 天气
	weather = response["now"]["text"]
	# 当前温度
	temp = response["now"]["temp"] + u"\N{DEGREE SIGN}" + "C"
	# 风向
	wind_dir = response["now"]["windDir"]
	return {
		"region": region,
		"weather": weather,
		"temp": temp,
		"wind_dir": wind_dir,
	}
