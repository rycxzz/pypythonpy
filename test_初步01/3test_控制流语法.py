# 分支结构  if语句
# a = 1
# if a == 0:
#     print("a=0")
# else:
#     print("a!=0")

# 多重分支，满足哪个条件就走哪个分支，当不满足以上任何条件时用else:
# a = 3
# if a == 0:
#     print("a=0")
# elif a == 1:
#     print("a=1")
# elif a == 2:
#     print("a=2")
# else:
#     print("a不等于0、1、2")

# 分支嵌套
# 如题：
# x > 1 时， y =3x-5
# -1 <= x <= 1 时， y = x+2
# x < -1 时， y = 5x+3
# # 分支结构--
# x = -2
# if x > 1:
#     y = 3*x-5
# else:
#     if x >= -1:
#         y = x+2
#     else:
#         y = 5*x+3
# print(y)
# 多重分支--
# x = 2
# if x > 1:
#     y = 3*x-5
# elif -1 <= x <= 1:
#     y = x+2
# elif x < -1:
#     y = 5*x+3
# print(y)