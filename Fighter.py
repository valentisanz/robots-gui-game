import random
from Robot import *
class Fighter(Robot):
    
    def __init__(self,name):
        self.name=name
        self.power=15
        self.magic=10
        self.health=100
        self.type='Fighter'

# f1=Fighter('Gotard')
# f2=Fighter('Kralamar')

# print(f1.name,'attacks')
# print(f'{f2.name}: -{f1.attack(f2)} PdV')
# Gotard attacks
# Enemy: -15 PdV

