# -*- coding: utf-8 -*-

import os
import sys

from classdefine import *

#根据项目类型创建文件夹
def createfile(type,name):
    if type==0:
        path=u'C:\\Users\\chenhui22\\Desktop\\记录\\测试记录\\2019\\一季度\\测试记录\\基础定制\\'+name
    elif type==1:
        path=u'C:\\Users\\chenhui22\\Desktop\\记录\\测试记录\\2019\\一季度\\测试记录\\小定制\\'+name

    os.makedirs(path)
    os.open(u'C:\\Users\\chenhui22\\Desktop\\压缩包')

def getfilename(path):
    filelist=os.listdir(path)


def main():
    u='start  C:\\Users\\chenhui22\\Desktop\\压缩包'
    os.system(u)
    os.start
    n='https://192.0.0.140/DVR-CustomPrj/NVR/海外/2018/201810/PJ01PC20181010023_土耳其RETRO DS-7604NI-E1 4P中性程序定制'
    c='C:\\Users\\chenhui22\\Desktop\\记录\\测试记录\\2019\\一季度\\测试记录\\小定制\\test测试'
    a = ziphandle('C:\\Users\\chenhui22\\Desktop\\压缩包','C:\\Users\\chenhui22\\Desktop\\串口')

    pathss=paths('C:\\Users\\chenhui22\\Desktop\\压缩包','C:\\Users\\chenhui22\\Desktop\\串口')
    a.deco()


if __name__=='__main__':
    main()
