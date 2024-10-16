# Python 标准库常见模块
# 操作系统相关：os
# 时间与日期：time、datetaime
# 科学计算：math
# 网络请求：urllib

# os模块主要针对文件、目录的操作
# os.mkdir()创建目录
# os.removedirs()删除文件
# os.getcwd()获取当前目录
# os.path.exists(dir or file)判断文件或者目录是否存在
import os

# os.mkdir("testdir")
# print(os.listdir("./"))
# os.removedirs("testdir")
# print(os.getcwd())
# print(os.path.exists("b"))
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt","w")
#     f.write("hello,os using")
#     f.close()

# time 模块
# 获取当前时间以及时间格式的模块
import  time

# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 获取两天前的时间
# now_time = time.time()
# two_day_before = now_time - 60*60*24*2
# time_tuple = time.localtime(two_day_before)
# print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))
# 获取三天后的时间
# now_time = time.time()
# three_dat_after = now_time+60*60*24*3
# time_tuple = time.localtime(three_dat_after)
# print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))

# urllib库
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.status)
# print(response.read())

# math库
import math
# 返回大于等于参数的最小整数
# print(math.ceil(5.5))
# 返回小于等于参数的最大整数
# print(math.floor(5.5))
# 平方根
# print(math.sqrt(15))
