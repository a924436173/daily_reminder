import os
from pathlib import Path

import yaml

from easydict import EasyDict


class ReminderConfig:
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self):
		_current_path = Path(__file__)
		_config_path = os.path.join(_current_path.parent.parent, "reminder_config.yaml")
		with open(_config_path, encoding='UTF-8') as yaml_file:
			_reminder_config = yaml.safe_load(yaml_file)
		self.config = EasyDict(_reminder_config)


config = ReminderConfig().config
