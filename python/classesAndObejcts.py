################Understanding classes & objects in python
#####
class Enemy:
    life = 3

    def attack(self):
        print('ouch')
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print('i am dead')
        else:
            print(str(self)+ "life left" )


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.atttack()
enemy1.check_life()
enemy2.check_life()
