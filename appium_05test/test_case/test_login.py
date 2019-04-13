from common.myunit import StartEnd
from businessView.loginView import LoginView

class TestLogin(StartEnd):
	def test_login(self):
		login=LoginView(self.driver,self.logger)
		login.login_action('leboxiaomei','leboxiaomei')
		import time
		time.sleep(5)
		login.logout_action()

if __name__=='__main__':
	testlogin=TestLogin()
	testlogin.test_login()