import  os  #Demo1_14.py
from util import my_config

ui = 'student.ui'   #被转换的ui文件
py = 'student.py'   #转换后的py文件
path = my_config.RESOUREC_DIR   #ui文件所在路径
os.chdir(path)  #将ui文件所在路径设置成当前路径
cmdTemplate = "PySide6-uic  {ui}  -o  {py}".format(ui=ui,py=py)  #文本模板
os.system(cmdTemplate)  #执行转换命令
