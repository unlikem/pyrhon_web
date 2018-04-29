import time
print(time.ctime())

t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", t))