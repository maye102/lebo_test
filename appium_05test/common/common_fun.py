from baseView.baseView import BaseView
from selenium.webdriver.common.by import  By
import os
import time

class Common(BaseView):
	cancelBtn = (By.ID, 'android:id/button2')
	skiptBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')


	def check_cancelBtn(self):
		try:
			cancelBtn=self.ele_is_visibility(self.cancelBtn)
		except:
			self.logger.info('没有取消升级按钮')
		else:
			cancelBtn.click()

	def check_skiptBtn(self):
		try:
			skiptBtn=self.ele_is_visibility(self.skiptBtn)
		except:
			self.logger.info('没有跳过按钮')
		else:
			skiptBtn.click()

	def get_size(self):
		x = self.driver.get_window_size()['width']
		y = self.driver.get_window_size()['height']
		return x, y

	def swipeLeft(self):
		size = self.get_size()
		x1 = int(size[0] * 0.9)
		y = int(size[1] * 0.5)
		x2 = int(size[0] * 0.2)
		self.driver.swipe(x1, y, x2, y, 1000)

	def getTime(self):
		return time.strftime("%Y-%m-%d %H_%M_%S")

	def getScreenShot(self,text):
		time=self.getTime()
		image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(text,time)
		self.logger.info('get %s screenshot' %text)
		self.driver.get_screenshot_as_file(image_file)

if __name__=='__main__':
	common=Common()
	common.check_cancelBtn()
	common.check_skiptBtn()
	common.getScreenShot('登录页面截图')