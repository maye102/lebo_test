import logging
from common.common_fun import Common
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class LoginView(Common):
	username_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
	password_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
	loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')

	commit=(By.ID,'com.tal.kaoyan:id/tip_commit')

	button_mysefl=(By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
	username=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

	RightButton=(By.ID,'com.tal.kaoyan:id/myapptitle_RightButton_textview')
	logoutBtn=(By.ID,'com.tal.kaoyan:id/setting_logout_text')

	Iknow_prompt=(By.ID,'com.tal.kaoyan:id/task_no_task')

	def login_action(self,username,password):
		self.check_cancelBtn()
		self.check_skiptBtn()

		# 判断是否有‘我’模块
		# login_status=self.check_loginStatus()
		# if login_status:
		# 	self.logout_action()
		#
		# self.ele_is_visibility(self.username).click()

		logging.info('============开始登录==============')
		logging.info('username is:%s' %username)
		self.ele_is_visibility(self.username_type).send_keys(username)

		logging.info('password is:%s'%password)
		self.ele_is_visibility(self.password_type).send_keys(password)

		logging.info('click loginBtn')
		self.ele_is_visibility(self.loginBtn).click()
		logging.info('login finished!')

	def check_prompt(self):
		try:
			Iknow=self.ele_is_visibility(self.Iknow_prompt)
		except:
			self.logger.info('没有"我知道"弹框')
		else:
			Iknow.click()

	def check_loginStatus(self):
		logging.info('====check_loginStatus======')
		try:
			self.ele_is_visibility(self.button_mysefl).click()
			nametext=self.ele_is_visibility(self.username).text
		except:
			logging.error('login Fail!')
			self.getScreenShot('login fail')
			return False
		else:
			if nametext == '未登录':
				return False
			else:
				logging.info('login success!')
				return True

	def logout_action(self):
		logging.info('=====logout_action======')
		self.ele_is_visibility(self.button_mysefl).click()
		self.ele_is_visibility(self.RightButton).click()
		self.ele_is_visibility(self.logoutBtn).click()
		self.ele_is_visibility(self.commit).click()

if __name__ == '__main__':
	driver,logger=appium_desired()
	login=LoginView(driver,logger)
	login.login_action('leboxiaomei','leboxiaomei')
	login.check_prompt()
	# import time
	# time.sleep(5)
	# login.logout_action()