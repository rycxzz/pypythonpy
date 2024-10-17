# 1.使用面向对象的实现一个回合制格斗游戏
# 一个回合制游戏，每个角色都有hp和power，初始值hp：1000，power：200
# 定义一个fight方法：
# final_hp = hp-enemy_power
# enemy_final_hp = enemy_hp-power
# 两个hp进行对比，血量剩余多的人获胜
# class Game:
#     hp = 1000
#     power = 200
#
#     def fight(self,enemy_hp,enemy_power):
#         final_hp = self.hp - enemy_power
#         enemy_final_hp = enemy_hp-self.power
#         if final_hp > enemy_final_hp:
#             print("我赢了")
#         elif final_hp < enemy_final_hp:
#             print("敌人赢了")
#         else:
#             print("平局")
#
# game = Game()
# game.fight(1000,200)

# 2.使用面向对象的继承改造游戏
# 将角色的hp、power通过传参传入
class Game:
    def __init__(self,hp,power):
        self.hp = hp
        self.power = power

    def fight(self,enemy_hp,enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp-self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")
# hp = 1000
# power = 200
#
# game = Game(hp,power)
# game.fight(1000,200)
# 第二个角色，他叫后裔，后裔继承了角色的hp和power。并多了护甲属性。
# houyi_hp = hp +defense-enemy_power
class HouYi(Game):
    ##如果在子类重新定义了__init__，那么父类的__init__将会被覆盖
    def __init__(self):
        ##解决方法
        super().__init__(1000,200)
        self.defense = 100

    def houyi_fight(self,enemy_power,enemy_hp):
        final_hp = self.hp + self.defense - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")

hp = 1000
power = 200
houyi = HouYi()
houyi.houyi_fight(hp,power)





