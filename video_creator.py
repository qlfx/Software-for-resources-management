import tkinter
import os
from selenium import webdriver

Chrome_Options = webdriver.ChromeOptions()

file_category = []



        

'''
function_file_starter_category = []
class file_starter
'''


path_vedio = "D:/Videos_For_Edit/"
folder_resouces = "/Resouces素材"
folder_dubbed = "/Dubbed配音"
folder_undubbed = "/Undubbed无配音"
folder_bgm = "/BGM"
folder_article = "/Article文案"
folder_check = "/Check校验"
article = "/文案.docx"

class file_starter_class:
    def __init__(self,vedio_name):
        self.name = vedio_name
    def file_starter(self):
        os.startfile(path_vedio + self.name)



window = tkinter.Tk()
window.title("视频工程文件准备")
window.geometry("1080x900")
label_videoname = tkinter.Label(window,text="视屏名称",font=("Arial",14),width= 30 ,height= 2)
label_videoname.grid(row=0,column=0)
entry_videoname = tkinter.Entry(window,show = None,font=('Arial',14))
entry_videoname.grid(row=1,column=0)

#label_reminder = tkinter.Label(window,text="输入1表示打开，输入2表示删除",font=("Arial",14),width= 30 ,height= 2)
#label_reminder.grid()
#entry_function = tkinter.Entry(window,show=None,font=("Arial",14))
#entry_function.grid()



def jy_starter():
    jy_path = "D:/jianying/JianyingPro/JianyingPro.exe"
    os.system(jy_path)

def refresh(video_name):
    i= len(file_category)
    
    file_starter_category.append(file_starter_class(video_name))
    file_category.append(tkinter.Button(window,text=video_name,command=file_starter_category[i].file_starter))
    file_category[i].grid()

def generate():
    video_name = entry_videoname.get()
    os.mkdir(path_vedio + video_name)
    os.mkdir(path_vedio + video_name + folder_article)
    os.mkdir(path_vedio + video_name + folder_bgm)
    os.mkdir(path_vedio + video_name + folder_check)
    os.mkdir(path_vedio + video_name + folder_dubbed)
    os.mkdir(path_vedio + video_name + folder_resouces)
    os.mkdir(path_vedio + video_name + folder_undubbed) 
    docx = open(path_vedio + video_name + folder_article + "/文案.docx",'w')
    docx.close()
    refresh(video_name)

def get_files():
    resource_path = "D:/Videos_For_Edit"
    counter = 1
    files = os.listdir(resource_path)
    num = len(files)
    #for i in files:
    #    print(i)
    return files

file_starter_category = []

def main_file_starter():
    os.startfile(path_vedio)

def jjdown_starter():
    jjdown_path = "C:/Users/25453/Desktop/唧唧down"
    os.startfile(jjdown_path)

def ps_starter():
    ps_path = '"D:\PhotoShop2022\Adobe Photoshop 2022\Photoshop.exe"'
    os.system(ps_path)

def ae_starter():
    ae_path = '"D:\AfterEffects2022\Adobe After Effects 2022\Support Files\AfterFX.exe"'
    os.system(ae_path)
#def file_starter(file_path):
#    os.startfile(path_vedio + file_path)
    
def test():
    print(1)

def show():
    botton_vedioname = tkinter.Button(window,text="生成视频工程文件夹",command=generate)
    botton_vedioname.grid()

    label_function = tkinter.Label(window,text="选择功能",font=("Arial",14),width= 30 ,height= 2)
    label_function.grid()

    button_jjdown = tkinter.Button(window,text="打开唧唧down",command=jjdown_starter)
    button_jjdown.grid()

    button_open_file = tkinter.Button(window,text = "打开总文件夹",command=main_file_starter)
    button_open_file.grid()
    botton_jianying = tkinter.Button(window,text = "打开剪映",command=jy_starter)
    botton_jianying.grid()

    button_photoshop = tkinter.Button(window,text="打开photoshop",command=ps_starter)
    button_photoshop.grid()

    button_ae = tkinter.Button(window,text="打开AE",command=ae_starter)
    button_ae.grid()

    label_occupy = tkinter.Label(window,text="选择打开的文件夹",font=("Arial",14),width= 30 ,height= 2)
    label_occupy.grid()

    files = get_files()
    counter = 0
    for i in files:
        file_starter_category.append(file_starter_class(i))
        file_category.append(tkinter.Button(window,text=i,command=file_starter_category[counter].file_starter))
        file_category[counter].grid()
        counter+=1
    window.mainloop()
def main():
    show()
main()