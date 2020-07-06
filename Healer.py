import random
from Robot import *
class Healer(Robot):
    
    def __init__(self,name):
        self.name=name
        self.power=10
        self.magic=15
        self.health=100
        self.type='Healer'


