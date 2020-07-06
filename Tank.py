import random
from Robot import *
class Tank(Robot):
    
    def __init__(self,name):
        self.name=name
        self.power=10
        self.magic=10
        self.health=130
        self.type='Tank'

