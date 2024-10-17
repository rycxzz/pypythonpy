# 创建类
# class Person():
#     name = "noname"
#
#     def get_name(self):
#         return self.name
# # 调用类的属性
# print(Person.name)
# # 实例化
# p = Person()
# print(p.name)
# print(p.get_name())
# # 修改类的属性
# p.name = "lili"
# print(p.name)

# 实例引用、实例变量
# 实例：类的一个具体对象，比如，车类是一个类，摩托车或者自行车就是车类的一个实例。类是抽象的，实例是具体的。
# 实例引用：给一个对象起一个别名，比如，a是对象，b是a的引用，则a和b的地址空间都是一样的，修改b，则a被同时修改。
# 实例变量：实例属性，在任意方法内部，以'self.变量名'的方式定义的变量。
# 实例变量只能通过对象名访问，无法通过类名访问
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender} 我在吃")

    def drink(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender} 我在喝")
    def run(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender} 我在跑")

doudou = Person("doudou",10,'male')
mimi = Person("mimi",15,'female')

print(doudou.name)
doudou.run()







