import random
class Robot():
    name=''
    power=0
    magic=0
    health=0

    def getInfo(self):
        return(self.name,self.health,self.power,self.magic)
    def attack(self,enemy):
        rnd=random.randint(5, 10)
        if(rnd==5 or rnd==10 ):
            rnd=random.randint(5, 10)
            dmg=self.power+rnd+2
            enemy.health=enemy.health-dmg
            return (f'-{dmg}')
        else:
            enemy.health=enemy.health-self.power
            return (f'-{self.power}')

    def heal(self):
        self.health=self.health+self.magic
        return (f'+{self.magic}')
