# for in 循环，常用于循环次数明确的
# 1.计算 1～100 求和
# 2.加入分支结构实现1～100之间偶数求和
# 3.使用python实现1～100之间的偶数求和
# -----1
# range是个函数
# result = 0
# for i in range(101):
#     result = result+i
# print(result)
# -----2
# result = 0
# for i in range(101):
#     if i%2==0:
#         result = result+i
# print(result)
# -----3
# result = 0
# for i in range(2,101,2):
#         result = result+i
# print(result)

# while循环，常用于循环次数不确定的
# a = 1
# while a == 1:
#     print("a==1")
#     a =a+1
# else:
#     print("a!=1")
#     print(a)

# break 和 continue 语句
# break 可以跳出 for 和 while 的循环，任何对应的循环else块将不执行
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)
# continue 用来告诉python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)

# 练习：猜数字游戏
# 计算机出一个1～100之间的随机数由人来猜，计算机根据人猜的数字分别，输出提示大一点/小一点/猜对了
# import random
#
# computer_number = random.randint(1,100)
# """print(computer_number)"""
# while True:
#     preson_number = int(input("请输入一个数字"))
#     if preson_number > computer_number:
#         print("大一点")
#     elif preson_number < computer_number:
#         print("小一点")
#     elif preson_number == computer_number:
#         print("猜对了")
#         break