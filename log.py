import logging.handlers
import logging


class GetLog:
	def __init__(self, log_abs_path):
		self.log_abs_path = log_abs_path
		self.logger = None

	def log(self, name, level):
		if self.logger is None:
			self.logger = logging.getLogger(name=name)
			self.logger.setLevel(logging.DEBUG)
			fm = "%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(lineno)d:%(message)s"
			fmt = logging.Formatter(fm)
			cl = logging.handlers.TimedRotatingFileHandler("{}".format(self.log_abs_path),
			                                               when="midnight",
			                                               interval=31,
			                                               encoding="utf8")
			cl.setLevel(level)
			cl.setFormatter(fmt)
			cl.suffix = "%Y-%m-%d"
			self.logger.addHandler(cl)
		return self.logger

	def debug(self):
		return self.log(name="debug", level="DEBUG")

	def info(self):
		return self.log(name="info", level="INFO")

	def warning(self):
		return self.log(name="warning", level="WARNING")

	def error(self):
		return self.log(name="error", level="ERROR")

	def critical(self):
		return self.log(name="critical", level="CRITICAL")


# 创建info级别的实例，单独的文件记录info日志
log_info = GetLog(log_abs_path="./info.log").info()

