# from common.myunit import StartEnd
# from businessView.loginView import LoginView
#
# class TestLogin(StartEnd):
# 	def test_login(self):
# 		print(1234567890)
# 		self.logger.info('test~')


from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
caps = {}
caps["platformName"] = "Android"
# caps["platformVersion"] = "5.1.1"
caps["deviceName"] = "127.0.0.1:62001"
caps["appPackage"] = "com.android.chrome"
caps["appActivity"] = "com.google.android.apps.chrome.Main"
caps["noReset"]=True

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
driver.implicitly_wait(10)

driver.get('https://m.baidu.com')
# sleep(10)
contexts=driver.contexts
print(contexts)
print(driver.current_context)
# driver.switch_to.context(contexts[-1])
print(driver.current_context)
# driver.execute(MobileCommand.SWITCH_TO_CONTEXT,{'name':"WEBVIEW_com.android.browser"})
text=driver.find_element_by_id('index-kw')
text.click()
text.send_keys(1234567890)
# driver.execute(MobileCommand.SWITCH_TO_CONTEXT,{'name':contexts[0]})
sleep(1)
TouchAction(driver).tap(x=300, y=345,count=2).release().perform()
