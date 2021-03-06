#coding:utf-8
import sys
curDir = sys.path[0]
sys.path.append(curDir + '\\common')
sys.path.append(curDir + '/common')

import Common
import Initialize
import TraverseEles
import unittest
from time import sleep


class TraverseMydetailPage(unittest.TestCase):

	def __init__(self,methodName):
		unittest.TestCase.__init__(self, methodName)
		self.lastEleIndex = 0
		self.currentEleIndex = 0
		self.desktopActivity = Common.getDesktopActivity()

		
		self.appPackage = 'com.yixia.videoeditor'         #设置被测试应用的包名
		self.appActivity = '.login.ui.SplashActivity'     #设置被测试应用的启动Activity
		self.testActivity = ".my.ui.MyPage"    #设置被测试应用的页面的activity
		print '************************** TraverseRebangPage test **************************'
		print Common.getDesktopActivity()

	#初始化操作
	def setUp(self):
		Common.setUp(self)

	#测试用例执行完成后的操作
	def tearDown(self):
		Common.tearDown(self)

	#初始化进入某个指定的页面进行遍历测试
	def goIntoPage(self):	
		Initialize.init_case(self)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/bottom_my').click()
		sleep(2)
		self.driver.find_element_by_id('com.yixia.videoeditor:id/info1').click()
		sleep(2)
		#判断当前Activity是否为被测试Activity，如果不是抛出异常，让用例执行失败
		if(Common.isTestActivity(self)):
			print "被测试的Activity为：" + self.driver.current_activity + ",是被测试的Activity"
		else:
			print "当前Activity为：" + self.driver.current_activity
			Common.excuteFailed("不是被测试activity")


	def test_traverse_mydetail_page(self):
		TraverseEles.traverse_all_elements(self)
		sleep(5)


def suite(self):
	suite = unittest.TestSuite()  
	suite.addTest(TraverseMydetailPage('test_traverse_mydetail_page'))
	runner = unittest.TextTestRunner()  
	runner.run(suite)
