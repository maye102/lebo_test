import unittest
from common.desired_caps import appium_desired
from baseView.baseView import BaseView
import logging
from time import sleep
import warnings

class StartEnd(unittest.TestCase,BaseView):
	def setUp(self):
		# 忽略警告
		warnings.simplefilter("ignore", ResourceWarning)
		self.driver, self.logger = appium_desired()
		self.logger.info('====setUp====')


	def tearDown(self):
		self.logger.info('====tearDown====')
		sleep(5)
		self.driver.quit()
if __name__=="__main__":
	StartEnd()