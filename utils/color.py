import random


def get_color():
	# 获取随机颜色
	get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
	color_list = get_colors(100)
	return random.choice(color_list)