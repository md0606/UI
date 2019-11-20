#coding=utf-8

#author=mengd

import unittest

from page.sina import *
from page.init import *
# from  selenium import webdriver
import time as t
from utills.operationXml import *



class SinaTest(Init,Sina):

    def test_sinaLogin_001(self,parent='divText',value='emailNull'):
        '''
        登录业务账号密码都为空
        '''
        self.login(' ',' ')
        self.assertEqual(self.getLoginError,self.getXmlUser(parent,value))
        print(self.getLoginError)

    def test_sinaLogin_002(self,parent='divText',value='emailFormat'):
        '''
        登录业务：输入不正确的用户名密码
        '''
        self.login('13233123','2222222')
        self.assertEqual(self.getLoginError,self.getXmlUser(parent,value))

if __name__ == '__main__':

    unittest.main(verbosity=2)
