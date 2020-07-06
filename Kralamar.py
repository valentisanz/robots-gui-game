import random
from Robot import *

class Kralamar(Robot):
    
    def __init__(self):
        self.name='Kralamar'
        self.power=13
        self.magic=11
        self.health=110
    def decision(self,enemy):
        if(self.health>50):
            rnd=random.randint(1, 3)
            if(rnd==2):
               return super().heal()
            else:
               return super().attack(enemy)
        else:
            rnd=random.randint(1, 4)
            if(rnd==2 or rnd==4):
               return super().attack(enemy)                
            else:
               return super().heal()