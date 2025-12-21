import tkinter
import os
import File_Tools
import GUI_Tools
import JSON_Tools

'''
Name:
输入参数:
输出参数:
功能：
备注:
'''

config = "config"                            #存放配置的文件叫做config.json,在安装目录下
JSON_Tools.JSON_INSTALLATION_INIT(config)  #存放配置的文件叫做config.json,在安装目录下

window_0 = GUI_Tools.open_window_0()
window_0.mainloop()