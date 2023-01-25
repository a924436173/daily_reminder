import os
import sys

from requests import get

from config.config import config
from utils.log import log_info


def get_access_token():
	# appId
	app_id = config.wechat.app_id
	# appSecret
	app_secret = config.wechat.app_secret
	post_url = (
		f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}")
	try:
		access_token = get(post_url).json()['access_token']
	except KeyError:
		log_info.error("获取access_token失败，请检查app_id和app_secret是否正确")
		os.system("pause")
		sys.exit(1)
	return access_token
