#coding=utf-8

#author=mengd

import os
import unittest
import HTMLTestRunner_cn
import time as t

def allTest():
    '''获取所有需要执行的测试用例'''
    suite=unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__),'testcase'),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite

def getNowTime():
    '''获取当前时间'''
    return t.strftime('%Y-%m-%d %H-%M-%S',t.localtime(t.time()))

def run():
    fileName=os.path.join(os.path.dirname(__file__),
'report',getNowTime()+'sinaReport.html')
    fp=open(fileName,'wb')
    runner=HTMLTestRunner_cn.HTMLTestRunner(
        stream=fp,
        title='UI自动化测试报告',
        description='UI自动化测试报告详细信息'
    )
    runner.run(allTest())

if __name__=='__main__':
    run()