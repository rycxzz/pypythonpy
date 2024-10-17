# 读取文件,简便写法，此方法可免写 f.close()
# with open('cc/cc','rt') as f :
#     print(f.readlines())
# read()      读取文件中所有内容，大文件无法使用
# readable()  判断文件的可读性
# readline()  每次读取一行
# readlines() 读取所有行内容，放置列表中
# import json
#
# json使用方法
# json.dumps(python_obj)  把数据类型转换成字符串
# 变量名1 = [{数据类型}]
# 变量名2 = json.dumps(变量名1，sort_keys=True 按key排序, indent=4 缩进)
#
# json.loads(json_string) 把字符串转换成json
# 变量名1 = [{字符串}]
# 变量名2 = json.loads(变量名1)
#
# json.dump()             把数据类型转换成字符串并存储在文件中
# 变量名 [{数据类型入josn}]
# json.dump(变量名，open("文件绝对路径","w（写入）"))
#
# json.load(file_stream)  把文件打开，把里面的字符串转换成数据类型
# 变量名 = json.load(open('文件绝对路径','r'))
# print(变量名[0]['某key的value'])
# print(变量名[1]['某key的value'])