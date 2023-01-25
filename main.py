import sys
import os

from config.config import config
from utils.access_token import get_access_token
from utils.log import log_info
from utils.send_msg import send_message
from utils.star import get_star_remind
from utils.weather import get_weather


def main():
	users = config.wechat.user  # 接收的用户
	params = {
		"access_token": get_access_token(),  # 获取accessToken
		"weather": get_weather(),  # 获取天气信息
		"star": get_star_remind()  # 星座提醒消息
	}

	# 公众号推送消息
	for user in users:
		send_message(user, params)
	os.system("pause")


if __name__ == "__main__":

	# from apscheduler.schedulers.blocking import BlockingScheduler
	try:
		log_info.info("start reminder ...")
		main()
		# sched = BlockingScheduler()
		# # 每日7.30提醒
		# sched.add_job(main, 'cron', hour=7, minute=30)
		# sched.start()
	except SyntaxError:
		log_info.error("推送消息失败，请检查配置文件格式是否正确")
		os.system("pause")
		sys.exit(1)
	except Exception as error:
		log_info.error("send failed: %s", error)
