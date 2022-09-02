import shutil
import os
def my_copy(path1,path2,type='file'):
    if type == 'file':
        shutil.copyfile(path1,path2)
        print('文件复制成功')
    elif type == 'dir1':
        shutil.copytree(path1,path2)
        print('目录复制成功')
    return
# 复制test2里面的test文件到day19下面
# my_copy('E:\Python学习\day18\\test\\test2\\test','E:\Python学习\day19\\test')
# 复制目录test及其test2及test到文件day19下面,命名:ceshi
# my_copy('E:\Python学习\day18\\test','E:\Python学习\day19\ceshi',type='dir1')
my_copy('F:\\泰安铂傲\myConfig\\xingye-backend-config\\business-admin-manager\\config','F:\\泰安铂傲\\myConfig\\test\\',type='dir1')
my_copy('F:\\泰安铂傲\myConfig\\xingye-backend-config\\business-customer-manager\\config','F:\\泰安铂傲\\myConfig\\test\\',type='dir1')
my_copy('F:\\泰安铂傲\myConfig\\xingye-backend-config\\business-flowable-test-manager\\config','F:\\泰安铂傲\\myConfig\\test\\',type='dir1')
my_copy('F:\\泰安铂傲\myConfig\\xingye-backend-config\\business-public-manager\\config','F:\\泰安铂傲\\myConfig\\test\\',type='dir1')