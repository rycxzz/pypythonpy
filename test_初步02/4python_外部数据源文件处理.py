# YAML用来表达数据序列化的格式，作为配置文件使用
# JSON轻量级数据交换语言，用于传输由属性值或者序列性的值组成的数据对象
# EXCEL直观的界面、计算功能和图表工具即可电子制表软件
import yaml

print(yaml.load("""
 - Hesperiidae
 - Papilionidae
 - Apatelodidae
 - Epiplemidae
 """,Loader=yaml.FullLoader))
print(yaml.dump({'a': [1, 2]}))











