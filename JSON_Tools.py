import os,sys
import json
import File_Tools

'''
Name:JSON_INSTALLATION_INIT
输入参数:file_name:需要检索的文件名称
输出参数:path1:json文件路径
功能:对安装路径下的json文件初始化,如果在路INSTALLATION_径中没有找到对应json文件,就创建一个
备注:检索的路径是文件的安装路径,这个可能在后期会导致一些开发问题,但是不管了
'''
def JSON_INSTALLATION_INIT(file_name):
    #current_file = __file__                    # 当前文件的路径
    if getattr(sys, 'frozen', False):
        # exe 模式
        current_file = os.path.dirname(sys.executable)
    else:
        # python 脚本模式
        current_file = os.path.dirname(os.path.abspath(__file__))
    #current_file = os.path.dirname(sys.executable)# 当前文件的路径
    #current_dir = os.path.dirname(current_file)  # 当前文件所在目录
    current_dir = current_file
    print(current_dir)
    file_name1 = file_name + ".json"
    path1 = os.path.join(current_dir,file_name1)
    if os.path.exists(path1):
        return path1
    else:
        with open(path1, "w", encoding="utf-8") as f:
            f.write("{}")   # 写一个空 JSON 对象,也可以写 ""
            f.close()
        return path1
'''
Name:JSON_Writer
输入参数:file_path json文件的路径,data要写入的数据,这里要经过path_complier转译
输出参数:
功能:根据输入框的内容对json文件进行修改
备注:
'''
def JSON_Writer(file_path,data):
    if not os.path.exists(file_path):
        return {}

    with open(file_path,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)

'''
Name:JSON_Reader
输入参数:file_path:json文件的路径
输出参数:json.load(f):json文件中的东西
功能:读取名为paths的json文件并且返回其中储存的路径列表
'''
def JSON_Reader(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        return json.load(f)
    
'''
Name:create_key
输入参数:file_path json文件的路径 key_name 需要输入的键的名字,在这里是路径, key_value 键值,在这里是习惯创建的文件名字
输出参数:
功能:在json文件中创建新的路径配置
备注:
'''
def create_key(file_path,key_name):
    data = JSON_Reader(file_path)
    init_value = None
    if key_name in data:
        return

    # 默认初始化为空列表（最常用）
    if init_value is None:
        init_value = []

    data[key_name] = init_value
    JSON_Writer(file_path,data)

'''
Name:add_value
输入参数:file_path json文件的路径,key_name要改变的键,这里是路径, value 要加的键值,这里是习惯的文件
输出参数:
功能：在对应的键下创建新的键值
备注:
'''
def add_value(file_path,key_name, value):
    """
    向 key 对应的列表中添加一个元素。
    若 key 不存在则报错。
    """

    data = JSON_Reader(file_path)

    if key_name not in data:
        print(f"错误：键 '{key_name}' 不存在，请先创建键。")
        return

    # 如果该键不是列表，也提醒用户
    if not isinstance(data[key_name], list):
        print(f"错误：键 '{key_name}' 的值不是列表，无法添加元素。")
        return

    data[key_name].append(value)
    JSON_Writer(file_path,data)

'''
Name:read_values
输入参数:file_pathjson文件的路径,key_name要读的键
输出参数:data[key_name],key_name下的键值
功能:读取json文件中的key_name下的键值
备注:
'''
def read_values(file_path,key_name):

    data = JSON_Reader(file_path)
    if key_name not in data:
        print(f"键 '{key_name}' 不存在")
        return None
    return data[key_name]

'''
Name:delete_key
输入参数:file_path json文件的路径,key_name 要删除的键
输出参数:
功能：
备注:
'''
def delete_key(file_path,key_name):

    data = JSON_Reader(file_path)
    if key_name in data:
        del data[key_name]
        JSON_Writer(file_path,data)
    else:
        print(f"键 '{key_name}' 不存在")

'''
Name:key_reader
输入参数:file_path json文件的位置
输出参数:keys,键值 主文件夹的路径
功能：
备注:
'''
def key_reader(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        data = json.load(f)
    keys = list(data.keys())
    return keys