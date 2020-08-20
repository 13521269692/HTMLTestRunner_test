# -*- coding: utf-8 -*-

"""HTMLTestRunner 截图版示例 selenium 版"""
from selenium import webdriver
import unittest
import time
from HTMLTestRunner_cn import HTMLTestRunner
import sys


class case_01(unittest.TestCase):
    """
    def setUp(cls):
        cls.driver = webdriver.Chrome()

    def tearDown(cls):
        cls.driver.quit()

        """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        # self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用例失败后截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass


    def test_case1(self):
        """
                        百度搜索
       
        """
        print("本次校验没过？")
        
        self.driver.get("https://www.baidu.com")
        self.add_img()
        self.driver.find_element_by_id('kw').send_keys(u'CSDN')
        self.add_img()
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        self.add_img()

    def test_case2(self):
        """CSDN首页"""
        self.driver.get("https://www.csdn.net")
        print("本次校验没过？")
        self.assertTrue(False,"这是相当的OK")

    def test_case3(self):
        """ PYTHON基础教程/菜鸟教程"""
        self.driver.get("https://www.runoob.com/python/python-tutorial.html")
        # self.imgs.append(self.driver.get_screenshot_as_base64())
        print("没法打印？")
        self.assertIn(u"中文", u'菜鸟','WYZ')

    def test_case4(self):
        u""" 菜鸟教程首页"""
        self.driver.get("https://www.runoob.com")
        raise Exception
        self.add_img()
        self.assertTrue(True)


class case_02(unittest.TestCase):
    """
    def setUp(cls):
        cls.driver = webdriver.Chrome()

    def tearDown(cls):
        cls.driver.quit()

        """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        # self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass


    def test_case1(self):
        """
                        百度搜索
       
        """
        print("本次校验没过？")
        
        self.driver.get("https://www.baidu.com")
        self.add_img()
        self.driver.find_element_by_id('kw').send_keys(u'CSDN')
        self.add_img()
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        self.add_img()

    def test_case2(self):
        """CSDN首页"""
        self.driver.get("https://www.csdn.net")
        print("本次校验没过？")
        self.assertTrue(False,"这是相当的OK")

    def test_case3(self):
        """ PYTHON基础教程/菜鸟教程"""
        self.driver.get("https://www.runoob.com/python/python-tutorial.html")
        # self.imgs.append(self.driver.get_screenshot_as_base64())
        print("没法打印？")
        self.assertIn(u"中文", u'菜鸟','WYZ')

    def test_case4(self):
        u""" 菜鸟教程首页"""
        self.driver.get("https://www.runoob.com")
        raise Exception
        self.add_img()
        self.assertTrue(True)



if __name__ == "__main__":
    from unittest import TestResult
    suite1 = unittest.TestLoader().loadTestsFromTestCase(case_01)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(case_02)
    suites =  unittest.TestSuite()
    suites.addTests([suite1,suite2])

    runer = HTMLTestRunner(title="带截图的HTML测试报告", description="测试详情", stream=open("sample_test_report.html", "wb"), verbosity=2, retry=2, save_last_try=True)
    runer.run(suites)
   
   
   
    '''
           可以根据需要更改  生成的HTML的路径和HTML文件名
           
    
    #获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
     #打开一个文件，将result写入此file中
    filename = r"D:\aa\{0}result.html".format(now)
    print(filename)
    fp = file(filename, 'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title = u'带截图的HTML测试报告', description = u'测试执行情况', retry=2,save_last_try=True)
    '''
    
    #在实例化HTMLTestRunner 对象时追加参数，retry，指定重试次数，如果save_last_try 为True ，一个用例仅显示最后一次测试的结果。
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title = u'带截图的HTML测试报告', description = u'测试执行情况', save_last_try=True)
    runer.run(suites) 









