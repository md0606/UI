#coding=utf-8

#author=mengd


import unittest
from selenium import webdriver

from utills.operationXml import *
class Init(unittest.TestCase,OperationXml):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.getXmlData('url'))
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()