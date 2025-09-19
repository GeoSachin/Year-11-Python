import random

class Fighter:
    def __init__(self, Name, AvgAttackDamage, Health): #Define the constructor with parameters model, year, and engine
        self.Name = Name
        self.AvgAttackDamage = AvgAttackDamage
        self.Health = Health
        self.__PrivateHealth = 100
Man1 = Fighter("Tom", 35, 100) #Creating the first character that will be used in the game
Man2 = Fighter("Yug", 30, 100) #Creating the second character that will be used in the game

RandomN = random.randint(0,1)

def Fight(Fighter1, Fighter2): #Creating a function that will make the two fighters fght
    if RandomN == 0:
     Fighter1.Health = Fighter1.Health-Fighter2.AvgAttackDamage-5 #Making fighter 2 stronger
     Fighter2.Health = Fighter2.Health-Fighter1.AvgAttackDamage
    else:
     Fighter1.Health = Fighter1.Health-Fighter2.AvgAttackDamage
     Fighter2.Health = Fighter2.Health-Fighter1.AvgAttackDamage-5 #Making fighter 1 stronger
    if Fighter1.Health <=0:
        print(Fighter1.Name + " has died.") #Showing that fighter one has died
    if Fighter2.Health <=0:
        print(Fighter2.Name + " has died.") #Showing that fighter two has died

while Man1.Health > 0 and Man2.Health > 0: #Checking that they are alive
   Fight(Man1,Man2) #Getting both of the people to fight
    