import os
import sys

from datetime import date
from zhdate import ZhDate

from utils.log import log_info


def get_birthday(birthday, year, today):
	birthday_year = birthday.split("-")[0]
	# 判断是否为农历生日
	if birthday_year[0] == "r":
		r_mouth = int(birthday.split("-")[1])
		r_day = int(birthday.split("-")[2])
		# 获取农历生日的今年对应的月和日
		try:
			birthday = ZhDate(year, r_mouth, r_day).to_datetime().date()
		except TypeError:
			log_info.error("请检查生日的日子是否在今年存在")
			os.system("pause")
			sys.exit(1)
		birthday_month = birthday.month
		birthday_day = birthday.day
		# 今年生日
		year_date = date(year, birthday_month, birthday_day)

	else:
		# 获取国历生日的今年对应月和日
		birthday_month = int(birthday.split("-")[1])
		birthday_day = int(birthday.split("-")[2])
		# 今年生日
		year_date = date(year, birthday_month, birthday_day)
	# 计算生日年份，如果还没过，按当年减，如果过了需要+1
	if today > year_date:
		if birthday_year[0] == "r":
			# 获取农历明年生日的月和日
			r_last_birthday = ZhDate((year + 1), r_mouth, r_day).to_datetime().date()
			birth_date = date((year + 1), r_last_birthday.month, r_last_birthday.day)
		else:
			birth_date = date((year + 1), birthday_month, birthday_day)
		birth_day = str(birth_date.__sub__(today)).split(" ")[0]
	elif today == year_date:
		birth_day = 0
	else:
		birth_date = year_date
		birth_day = str(birth_date.__sub__(today)).split(" ")[0]
	return birth_day
