# 获取异常
# try里需要执行的代码，except里是发生异常要执行的代码，else里是无异常执行的代码，finally里是无论是否有异常都执行的代码
# try:
#     num1 = int(input("输入一个除数"))
#     num2 = int(input("输入一个被除数"))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("这是一个异常")
# except:
#     print("这是一个通用型异常")
# else:
#     print("没有异常")
# finally:
#     print("无论发没发生异常，都执行")
#
# # 抛出异常 raise
# x = 10
# if x > 5:
#     raise Exception("这是抛出的异常信息")

# 自定义异常
# class MyException(Exception):
#     def __init__(self,value1,value2):
#         self.value1 = value1
#         self.value2 = value2
#
# raise MyException("value1","value2")





