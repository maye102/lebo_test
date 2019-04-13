from common.desired_caps import appium_desired
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BaseView(object):

	def __init__(self,driver,logger):
		self.driver=driver
		self.logger=logger
		self.wait=WebDriverWait(self.driver,10)

	# 元素是否可见（单个元素）
	def ele_is_visibility(self, eletuple):
		try:
			ele = self.wait.until(EC.visibility_of_element_located(eletuple))
			return ele
		except:
			self.logger.error(u'ele_is_visibility:未找到元素 %s' % eletuple)

	# 返回一组数据(list)
	def get_eles(self, eletuple):
		try:
			ele = self.wait.until(EC.visibility_of_all_elements_located(eletuple))
			return ele
		except:
			self.logger.error(u'ele_is_presence：未找到元素 %s ' % eletuple)


if __name__=='__main__':
	BaseView()