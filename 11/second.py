# 自动安装第三方库
import os
libs = {"numpy"}

try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Success")
except:
    print("Fail")