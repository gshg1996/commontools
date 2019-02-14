# -*- coding: utf-8 -*-
import zipfile
import os

class paths:
    def __init__(self,zippath,serialpath):
        self.zippath=zippath.decode('utf-8')
        self.serialpath=serialpath.decode('utf-8')

class project:
    proid=''#项目id
    name=''#项目名字
    version=''#软件版本

    def __init__(self,url,zipname):
    #svn的url，解压文件名字
        self.url=url
        self.zipname=zipname


    def getinfo(self):
    #获取项目ID和项目名字
        pos=0
        cpos=0
        for i in self.url[::-1]:
            cpos+=1
            if i!='/':
                if i=='_':
                    pos=cpos
                self.name=i+self.name
            else:break
        self.proid=self.name[0:cpos-pos-1]
    #获取软件版本
        cpos=0
        for i in self.zipname[::-1]:
            cpos+=1
            if i=='V':
                if self.zipname[len(self.zipname)-cpos-1]=='_':
                    break
        self.version=self.zipname[len(self.zipname)-cpos:len(self.zipname)]
        print(self.version)


class ziphandle:
    zipname=''

    def __init__(self,path,depath):
    #压缩包位置和目标位置
        self.path=path.decode('utf-8')
        self.depath=depath.decode('utf-8')

    def deco(self):
    #解压文件到指定位置
        filelist=os.listdir(self.path)
        self.zipname=filelist[0]
        os.chdir(self.path)
        f=zipfile.ZipFile(filelist[0])
        f.extractall(self.depath)




