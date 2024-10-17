from game.game import Game


class HouYi(Game):
    ##如果在子类重新定义了__init__，那么父类的__init__将会被覆盖
    def __init__(self):
        ##解决方法
        super().__init__(1000,200)
        self.defense = 99

    def houyi_fight(self,enemy_power,enemy_hp):
        while True:
            self.hp = self.hp + self.defense - enemy_power
            # print("我的最终血量{}".format(final_hp))
            enemy_hp = enemy_hp - self.power
            print(self.hp)
            print(enemy_hp)
            if self.hp <= 0:
                print("我输了")
                break
            elif enemy_hp <= 0:
                print("敌人输了")
                break
            # else:
            #     raise Exception("没有平局！！！！！")

hp = 1000
power = 200
houyi = HouYi()
houyi.houyi_fight(hp,power)