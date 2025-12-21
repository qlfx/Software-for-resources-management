import tkinter
import File_Tools
import JSON_Tools
import subprocess, sys
import os

config = "config"       #存放配置的文件叫做config.json,在安装目录下
col = 0   #这个是控制王窗口排版的
'''
Name:open_window_0
输入参数:
输出参数:window_0:创建的王窗口的名字
功能：创建王窗口
备注:
'''
def open_window_0():
    window_0 = tkinter.Tk()
    window_0.title("总控界面,交流、bug反馈:bilibili沙河寄居蟹,邮箱:a737001zlfxwwy@163.com")
    window_0.geometry("1080x900")
    window_0_button_settings = tkinter.Button(window_0,text="配置路径点这里",width=20, height=2,command=lambda:open_settings(window_0))
    window_0_button_settings.grid()
    path_shower(JSON_Tools.JSON_INSTALLATION_INIT(config),window_0,col)
    return window_0

'''
Name:open_settings
输入参数:great_window:上一级的窗口,现在小型开发默认是window_0
输出参数:settings:将军窗口
功能：创建一个将军窗口
备注:
'''
def open_settings(great_window):
    settings = tkinter.Toplevel(great_window)
    settings.title("路径设置")
    settings.geometry("1000x800")
    label_settings = tkinter.Label(settings,text="配置路径")#"配置路径按钮"
    label_settings.grid()
    path_entry = tkinter.Entry(settings,show=None,font=('Arial,14'))
    path_entry.grid()
    
    buttun_add_path = tkinter.Button(settings,text="添加一条路径",command=lambda:input_path_settings(settings,path_entry))#添加路径的按钮
    buttun_add_path.grid()
    button_close = tkinter.Button(settings,text="设置好了！",command=settings.destroy)#关闭界面按钮
    button_close.grid()
    setting_shower(JSON_Tools.JSON_INSTALLATION_INIT(config),settings)
    return settings

'''
Name:input_path_settings
输入参数:settings_window 窗口名字,entry 窗口的输入框名字
输出参数:
功能：根据输入框的路径创建按钮,按钮可以创建士兵窗口,并且在json文件中加入键值,加入键值之后能
备注:
'''
def input_path_settings(settings_window,entry):
    path = tkinter.Button(settings_window,text=entry.get(),command=lambda:open_habits(settings_window,entry.get()))#创建对应文件习惯的按钮
    button_name = entry.get() #是按钮的名字 也是这个文件路径的名字
    the_files = File_Tools.traversal(button_name)#用来判断是否存在重复创建文件
    JSON_Tools.create_key(JSON_Tools.JSON_INSTALLATION_INIT(config),button_name)
    '''
    Name:open_habits
    输入参数:
    输出参数:
    功能：创建士兵窗口
    备注:
    '''
    def open_habits():
        habits = tkinter.Toplevel(settings_window)
        habits.title(button_name)
        file_entry = tkinter.Entry(habits,show=None,font=('Arial,14'))#输入要创建的文件的名字
        file_entry.grid()
        #这个按钮的功能是向json文件中写入文件配置的习惯
        button_add_habit_file = tkinter.Button(habits,text="添加要加入的文件名称(文件带后缀，文件夹不用)",command=lambda:habbit_adder(JSON_Tools.JSON_INSTALLATION_INIT(config),button_name,file_entry.get(),file_entry,habits))
        button_add_habit_file.grid()
        button_close = tkinter.Button(habits,text="设置好了！",command=habits.destroy)#关闭界面按钮
        button_close.grid()

        '''
        Name:shutdown
        输入参数:
        输出参数:
        功能：关闭当前窗口并且删除对应的按钮,还要删除对应的json文件的数据
        备注:
        '''
        def shutdown():
            JSON_Tools.delete_key(JSON_Tools.JSON_INSTALLATION_INIT(config),button_name)
            path.destroy()
            habits.destroy()
        button_delete = tkinter.Button(habits,text="删除这个路径",command=shutdown)
        button_delete.grid()
        habbit_shower(button_name,habits)
        habits.geometry("800x600")
        return habits
    entry.delete(0,'end')
    path.config(command=open_habits)
    path.grid()
    
'''
Name:habbit_shower
输入参数:key_name 要查询的键,window 显示的窗口
输出参数:
功能：在士兵窗口展示配置的常用文件
备注:
'''
def habbit_shower(key_name,window):
    habits = JSON_Tools.read_values(JSON_Tools.JSON_INSTALLATION_INIT(config),key_name)
    for i in habits:
        tkinter.Label(window,text=i,font=("Arial",12)).grid()

'''
Name:habbit_adder
输入参数:file_path json文件的路径
        key_name 键
        value,entry,window
输出参数:
功能:在json文件中加入键值,并且清空输入框
备注:
'''
def habbit_adder(file_path,key_name, value,entry,window):
    JSON_Tools.add_value(file_path,key_name,value)
    tkinter.Label(window,text=value,font=("Arial,12")).grid()
    entry.delete(0,'end')

'''
Name:setting_shower
输入参数:file_path json文件的路径
        key_name 键
输出参数:
功能:把json文件中的键读出来,在将军窗口创建按钮,按钮可以创建士兵窗口
备注:
'''
def setting_shower(file_path,settings_window):
    open_believer_cat = []#用来存不同的函数
    button_cat = []     #用来存不同的button
    list = JSON_Tools.key_reader(file_path)
    num = len(list)
    counter = 0
    used_shutdown = 0
    for text in list:
        button_cat.append(tkinter.Button(settings_window,text=text))
        def make_open_believer(settings_window,text):
            def open_believer():
                believer = tkinter.Toplevel(settings_window)
                believer.title(text)
                file_entry = tkinter.Entry(believer,show=None,font=("Arial,14"))
                file_entry.grid()
                button_add_habit_file = tkinter.Button(believer,text="添加要加入的文件名称(文件带后缀，文件夹不用)",command=lambda:habbit_adder(JSON_Tools.JSON_INSTALLATION_INIT(config),text,file_entry.get(),file_entry,believer))
                button_add_habit_file.grid()
                button_close = tkinter.Button(believer,text="设置好了！",command=believer.destroy)#关闭界面按钮
                button_close.grid()
                '''
                Name:shutdown
                输入参数:believer窗口名 button按钮名
                输出参数:
                功能:删除对应的窗口
                备注:
                '''
                def shutdown(believer,button):
                    JSON_Tools.delete_key(JSON_Tools.JSON_INSTALLATION_INIT(config),text)
                    button.destroy()
                    believer.destroy()

                button_delete = tkinter.Button(believer,text="删除这个路径",command=lambda:shutdown(believer,button_cat[list.index(believer.title())]))
                button_delete.grid()
                habbit_shower(text,believer)
                believer.geometry("800x600")
            return open_believer
        open_believer_cat.append(make_open_believer(settings_window,text))
        button_cat[counter].config(command=open_believer_cat[counter])
        button_cat[counter].grid()
        counter += 1

'''
Name:path_shower
输入参数:json_path json文件的路径
        god_window 王窗口
输出参数:
功能:在王窗口显示按钮,按钮能打开文件夹
备注:
'''
def path_shower(json_path,god_window,col):
    counter = 0
    row = 2
    creating_entry = tkinter.Entry(god_window,show=None,font=("Arial,14"))
    creating_entry.grid()
    list = JSON_Tools.key_reader(json_path)
    main_button_cat = []#存总button的
    button_cat = [] #存小button的
    open_main_file_cat = []#存开总文件夹函数的
    open_file_cat = []#存开小文件夹函数的


    for main_text in list:              #这个是用来生成总文件夹的按钮的
        main_button_cat.append(tkinter.Button(god_window,text=main_text))

        '''
        name:meke_open_file
        输入参数:godwindow,text
        输出参数:
        功能:先检测输入框是否有输入,如果没有，就打开对应的文件夹,如果有,就创建输入框中名字的文件
        '''
        def make_open_file(godwindow,text):
            def open_main_file():
                    file_name = creating_entry.get()
                    creating_entry.delete(0,'end')
                    if file_name == '':
                        os.startfile(text)
                    else:
                        os.makedirs(text+'\\'+file_name)
                        files_to_create_table = JSON_Tools.read_values(JSON_Tools.JSON_INSTALLATION_INIT(config),text)
                        for file_to_create in files_to_create_table:
                            File_Tools.generate(text+'\\'+file_name,file_to_create)
                        print(text+'\\'+file_name)
            return open_main_file
        open_main_file_cat.append(make_open_file(god_window,main_text))
        main_button_cat[counter].config(command=open_main_file_cat[counter])
        main_button_cat[counter].grid()
        counter += 1

    refresh_button = tkinter.Button(text="刷新！")

    def refresh():
        temp = 0
        
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()
    refresh_button.config(command=refresh)
    refresh_button.grid()