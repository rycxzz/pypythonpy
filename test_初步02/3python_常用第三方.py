# pytest 测试框架
# requests 网络访问库
import requests

r = requests.get("http://www.baidu.com")
print(r.status_code)
# 返回编码
r.encoding = "utf-8"
# 返回值
print(r.text)