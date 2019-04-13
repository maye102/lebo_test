import logging,random
from common.desired_caps import appium_desired
from  common.common_fun import Common,By
from businessView.loginView import LoginView


class RegisterView(Common):
	register_text=(By.ID,'com.tal.kaoyan:id/login_register_text')
	#头像设置相关元素
	userheader=(By.ID,'com.tal.kaoyan:id/activity_register_userheader')
	item_image=(By.ID,'com.tal.kaoyan:id/item_image')
	save=(By.ID,'com.tal.kaoyan:id/save')

	#用户名密码邮箱相关元素
	register_username= (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
	register_password= (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
	register_email= (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
	register_btn= (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')

	# 完善资料
	school = (By.ID, 'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
	major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
	goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

	# 院校相关元素
	university_search = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
	item_name = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')

	#专业相关元素
	major_subject_title = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
	major_search_item_name = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')
	major_group_title=(By.ID,'com.tal.kaoyan:id/major_group_title')

	#用户中心相关元素
	button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
	username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

	def register_action(self,register_username,register_password,register_email):
		login_view = LoginView(self.driver, self.logger)
		self.check_cancelBtn()
		self.check_skiptBtn()

		# 设置头像
		logging.info('======register_action======')
		self.ele_is_visibility(self.register_text).click()
		# logging.info('set userhead')
		# self.ele_is_visibility(self.userheader).click()
		# self.ele_is_visibility(self.item_image)[1].click()
		# self.ele_is_visibility(self.save).click()

		# 输入注册信息
		logging.info('username is %s'%register_username)
		self.ele_is_visibility(self.register_username).send_keys(register_username)

		logging.info('password is %s' % register_password)
		self.ele_is_visibility(self.register_password).send_keys(register_password)

		logging.info('email is %s' % register_email)
		self.ele_is_visibility(self.register_email).send_keys(register_email)

		self.ele_is_visibility(self.register_btn).click()

	def add_register_info(self):
		logging.info('======add_register_info=====')

		logging.info('select school...')
		self.ele_is_visibility(self.school).click()
		self.get_eles(self.university_search)[0].click()
		self.get_eles(self.item_name)[0].click()

		logging.info('select major...')
		self.ele_is_visibility(self.major).click()
		self.get_eles(self.major_subject_title)[0].click()
		# 判断列表中是否还需要展开列表
		try:
			self.ele_is_visibility(self.major_group_title)
		except:
			pass
		else:
			self.get_eles(self.major_group_title)[0].click

		self.get_eles(self.major_search_item_name)[0].click()
		self.ele_is_visibility(self.goBtn).click()

if __name__ == '__main__':
	import time
	time=int(time.time())
	driver,logger=appium_desired()
	register=RegisterView(driver,logger)
	login_view = LoginView(driver,logger)

	username = 'lebo' + str(time)
	password = 'lebo123456'
	email = 'lebo'+ str(time) + '@163.com'

	register.register_action(username,password,email)
	register.add_register_info()
	print(login_view.check_loginStatus())








