# 变量，a = 1 b = 2 等同于如下
# a,b = 1,2
# print(a)
# print(b)

# 数字:整型，浮点型，复杂型
# int_a = 1
# float_a = 2.1
# complex_a =2j
# print(type(int_a))
# print(type(float_a))
# print(type(complex_a))

# 字符串的使用
# \:转义符，如\n 是换行
# r:忽略转义符的作用，如\n,在 a = r'string@!@#$145\n',时忽略\直接被打印,否则a = 'strong@!@#$145\n'
# +以及空格：用于多个字符串连接
# 例如：a = "aaaaa" b = "bbbbb"
# 打印：print（a+b） 与 print（"aaaaa" "bbbbb"）效果一致，+号只能用作于变量
# f+{}/format：引用语法
# 场景：在b的字符串中引用a的字符串
# a = "aaaaa"
# b = f"bbbbb{a}"
# print(b) 结果：bbbbbaaaaa
# 第二种方法：
# a = "aaaaa"
# b = "bbbbb{}"
# print(b.format(a)) 结果：bbbbbaaaaa
# 多变量打印
# a = "aaaaa"
# c = "ccccc"
# b = "bbbbb{}{}"
# print(b.format(a,c)) 结果：bbbbbaaaaaccccc
# 更多变量打印
# a = "aaaaa"
# c = "ccccc"
# b = "bbbbb{x}{y}"
# print(b.format(x=a,y=c)) 结果：bbbbbaaaaaccccc

# 列表索引的使用，从0开始取值，最后面的可以用-1取值
# 列表使用中括号表示，打印时，索引也要用中括号
# list_a = [1,2,"a","b"]
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])
# print(list_a[-1])
# 切片索引,想要取第一位到第三位的值
# print(list_a[0:3])
