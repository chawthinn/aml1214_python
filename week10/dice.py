# dice module
import random 

class Die: 
    def __init__(self):
        self.value = 1 # default value is 1
    
    def roll(self):
        self.value = random.randrange(1, 7) # randomly generate number 1 to 6

class Dice:
    def __init__(self):
        self.list = [] # create an empty list
    
    def addDie(self, die):
        self.list.append(die) # append all generated die to list
    
    def rollAll(self): 
        for die in self.list: # then assign the randomly generated values as a list
            die.roll() # call roll method of die to randomly get number 1 to 6