import time
from businessView.registerView import RegisterView
from common.myunit import StartEnd

class TestRegister(StartEnd):
	def test_register(self):
		now=int(time.time())
		register=RegisterView(self.driver,self.logger)

		username = 'lebo' + str(now)
		password = 'lebo123456'
		email = username + '@163.com'

		register.register_action(username,password,email)
		register.add_register_info()




