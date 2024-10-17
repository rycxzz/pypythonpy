# 列表
# python中可以通过组合一些值，得到多种复合数据类型
# 列表通过[]号括起来，逗号分隔的一组值得到
# 一个列表可以包含不同类型的元素，但通常使用时各个元素类型相同
# ---列表的特性
# list.append(x):在列表的末尾添加一个元素。相当于a[len(a):] = [x]
# list_liebiao=[1,2,3]
# list_liebiao.append(0)
# print(list_liebiao)
# list.insert(i,x):在给定的位置插入一个元素。第一个参数是要插入的元素的索引，以a.insert(0,x)插
# 入列表头部，a.insert(len(a),x)等同于a.append(x)
# list_liebiao=[1,2,3]
# list_liebiao.insert(1,0)
# print(list_liebiao)
# list.remove(x):移除列表中第一个值为x的元素。如果没有这样的元素，则抛出ValueError异常。
# list_liebiao=[1,2,3]
# list_liebiao.remove(1)
# print(list_liebiao)
# list.pop([i]):删除列表中给定位置的元素并返回ta.ruguo没有给定位置，a.pop()将会删除并返回列表中的最后一个元素
# list_liebiao=[1,2,3]
# y = list_liebiao.pop(0)
# print(y)
# print(list_liebiao)
# list.sort(key=None,reverse=False):对列表中的元素进行排序（参数可用于自定义排序，解释参考sorted()）。
# 升序：
# list_liebiao=[1,5,6,7,2,3]
# list_liebiao.sort()
# print(list_liebiao)
# 降序：
# list_liebiao=[1,5,6,7,2,3]
# list_liebiao.sort(reverse=True)
# print(list_liebiao)
# list.reverse():反转列表中的元素
# list_liebiao=[1,5,6,7,2,3]
# list_liebiao.reverse()
# print(list_liebiao)
# list.clear()删除列表中所有的元素，相当于del a[:]。
# list.extend(iterable):使用可迭代对象中的所有元素来扩展列表。相当于a[len(a):] = iterable。
# list.index(x[,start[,end]])
# 返回列表中第一个值为x的元素的从零开始的索引。如果没有这样的元素将会抛出ValueError异常。
# 可选参数start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是start参数
# list.count(x):返回元素x在列表中出现的次数
# list.copy():返回列表中的一个浅拷贝，相当于a[:]
# 注意：
# insert、remove或者sort方法，只修改列表，没有打印出返回值--他们返回默认值None。这是Python中所有可变数据结构的设计原则
# 并非所有数据或可以排序或比较（字符串和数字等）
# ---列表推导式
# 生成一个平方列表，比如[1,4,9...]
# for循环：
# list_square=[]
# for i in  range(1,4):
#     list_square.append(i**2)
# print(list_square)
# 列表推导式：
# list_square=[]
# list_square = [ i**2 for i in range(1,4)]
# print(list_square)
# 列表推导式分支
# list_square = []
# list_square=[ i**2 for i in range(1,4) if i != 1 ]
# print(list_square)
# 列表推导式嵌套
# list_square = []
# for i in range(1,4):
#     for j in range(1,4):
#         list_square.append(i*j)

# list_square = [ i*j for i in range(1,4) for j in range(1,4) ]
# print(list_square)

# 元组
# 使用()进行定义
# tuple、list、range 都是序列数据类型。
# 元组是不可变的，可以通过解包、索引来访问
# tuple_ss = (1,2,3)
# tuple_ss2 = 1,2,3
# print("tuple_ss", tuple_ss)
# print(type(tuple_ss))
# print("tuple_ss2", tuple_ss2)
# print(type(tuple_ss2))
# 元组的不可变特性，特殊情况如果元组里嵌套了列表，那么嵌套的列表内容是可变的
# a = [1,2,3]
# tuple_ss = (1,2,a)
# tuple_ss[2][0]= "a"
# print(tuple_ss)
# 元组内置函数
# ---count 统计元组中某个元素的总数量
# a = (1,2,"a","a")
# print(a.count("a"))
# ---index 求出对应元素的索引值，如果存在多个相同元素，以第一个为准
# a = (1,2,3,"a","a")
# print(a.index("a"))

# 集合
# 是由不重复元素组成的无序的集
# 基本用法包括成员检测和消除重复元素
# 使用{}或者set()函数创建集合
# 要创建一个空集合只能用set()而不能用{}
# a = {1}
# b = set()
# print(len(b))
# print(type(a))
# print(type(b))
# 集合内置函数
# union 并集，a和b集合中的元素相加，然后去重，既是集合并集
# a = {1,2,3}
# b = {1,4,5}
# print(a.union(b))
# intersection 交集，a和b集合中相同的元素，既是集合交集
# a = {1,2,3}
# b = {1,4,5}
# print(a.intersection(b))
# difference 差集，a集合中有的元素，但在b集合中没有的元素，既是集合差集
# a = {1,2,3}
# b = {1,4,5}
# print(a.difference(b))
# add 添加元素
# a = {1,2,3}
# b = {1,4,5}
# a.add("a")
# print(a)
# 集合推导式 求出字符串去重后的集合
# print({i for i in "sdlkfjslkdjfsfffflkdj"})
# set()普通去重
# c = "sdlkjflwkejflkjdfffffffsd"
# print(set(c))

# 字典定义用{}号
# 以【关键字】为索引
# 【关键字】可以使任意不可变类型，通常是字符或数字。如果一个元组只包含字符串、数字或元组,那么这个元组也可以用作关键字
# ss_cc = {"a":1,"b":2}
# ss_cc2 = dict(a=1,b=2)
# print("ss_cc",ss_cc)
# print(type(ss_cc))
# print("ss_cc2",ss_cc2)
# print(type(ss_cc2))
# 获取元素的key值以及Value值。key值是不可变的，字典精髓就是键值对
# a = dict(a=1,b=2)
# print(a.keys())
# print(a.values())
# popitem随机删除一个键值对。【没看出随机的效果】
# a = dict(a=1,b=2)
# print(a.popitem())
# print(a)
# fromkeys分别把列表中的参数当做一个key值，建立一个新的列表，除此之外传第二个参数Value值“a”，组成键值对
# a = {}
# b = a.fromkeys([1,2,3],"a")
# print(b)
# 推导式
# print({i: i * 2 for i in range(1, 3)})