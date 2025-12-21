#To store some special functions
import os
import json

'''
Name:path_compier
输入参数:path
输出参数:s2:经过转译后的字符串
功能:将windows路径中的'\'转换为'\'
'''
def path_complier(path):
    s2 = path.replace('\\', '/')
    return s2

'''
Name:traversal
输入参数:file_path,需要遍历的路径
输出参数:file_names:路径下的所有文件的列表
功能：遍历指定路径下的所有文件
'''
def traversal(path):
    counter = 1
    file_path = path_complier(path)
    file_names = os.listdir(path)
    return file_names

'''
Name:generate
输入参数:path 指定的路径,file_name 指定文件的名字(带后缀)
输出参数:
功能:在指定的路径创建指定的文件
备注:
'''
def generate(path,file_name):
    if file_name in traversal(path):
        return
        
    else:
        if '.' in file_name:
            file = open(path + "\\" + file_name,'w')
            file.close
        else:
            os.mkdir(path + "\\" + file_name)
