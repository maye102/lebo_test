from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
import yaml
import os
import logging
import logging.config

def appium_desired():
	filelpath=os.path.dirname(os.path.dirname(__file__))
	config_file=open(filelpath+'/config/logger.ini',encoding='utf-8')
	logging.config.fileConfig(config_file)
	logger=logging.getLogger('infoLogger')

	with open(filelpath+'/config/desired_caps.yaml','r',encoding='utf-8') as yaml_file:
		data=yaml.load(yaml_file)
	# print(type(data))
	# print(data['a'])
	# print(data['a']['b'])

	caps = {}
	caps["platformName"] = data['platformName']
	caps["platformVersion"] = data['platformVersion']
	caps["deviceName"] = data['deviceName']
	caps["appPackage"] = data['appPackage']
	caps["appActivity"] = data['appActivity']
	# caps["noReset"]=data["noReset"]
    #app_path = os.path.join(filelpath, 'app', data['appname'])
    #desired_caps['app']=app_path
	logger.warning('初始化设置')
	driver=webdriver.Remote('http://'+str(data["ip"])+":"+str(data["port"])+"/wd/hub",caps)

	return driver,logger

if __name__=='__main__':
	driver,logger=appium_desired()
	logger.info(1234)