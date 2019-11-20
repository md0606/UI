#coding=utf-8
#author = mengd

import os
import xml.dom.minidom

class OperationXml(object):
    def dir_base(self,fileName,filePath='data'):
        '''
        获取data文件夹下的文件
        :param fileName: 要读取的文件名称
        :param filePath: 要读的文件名对应的文件夹
        :return:
        '''
        return os.path.join(os.path.dirname(
            os.path.dirname(__file__)),filePath,fileName)
    def getXmlData(self,value):
        '''
        获取xml单节点的数据
        :param value: 文件单节点的名称
        :return:
        '''
        dom=xml.dom.minidom.parse(self.dir_base('ui.xml'))
        db=dom.documentElement
        name=db.getElementsByTagName(value)
        nameValue=name[0]
        return nameValue.firstChild.data

    def getXmlUser(self,parant,child):
        '''
        获取xml子节点的数据
        :param parant: 文件中父节点的名称
        :param child: 文件中子节点的名称
        :return:
        '''
        dom = xml.dom.minidom.parse(self.dir_base('ui.xml'))
        db = dom.documentElement
        itemlist=db.getElementsByTagName(parant)
        item = itemlist[0]
        return item.getAttribute(child)