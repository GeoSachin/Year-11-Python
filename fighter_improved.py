import random
TomDeath = 0
YugDeath = 0
loopCount = 0

class Fighter:
    def __init__(self, Name, AvgAttackDamage, Health): #Define the constructor with parameters model, year, and engine
        self.Name = Name
        self.AvgAttackDamage = AvgAttackDamage
        self.Health = Health
        self.__PrivateHealth = 100
        self.Deaths = 0
Man1 = Fighter("Tom", 12, 100) #Creating the first character that will be used in the game
Man2 = Fighter("Yug", 13, 100) #Creating the second character that will be used in the game

RandomN = random.randint(0,3)

def Fight(Fighter1, Fighter2): #Creating a function that will make the two fighters fght
    if RandomN == 0:
     Fighter1.Health = Fighter1.Health-Fighter2.AvgAttackDamage-5 #Making fighter 2 stronger
     Fighter2.Health = Fighter2.Health-Fighter1.AvgAttackDamage
     print(str(Fighter2.Name) + " dealt " + str(Fighter2.AvgAttackDamage-5) + " damage to " + str(Fighter1.Name))#Printing the damage dealt
     print(str(Fighter1.Name) + " dealt " + str(Fighter1.AvgAttackDamage) + " damage to " + str(Fighter2.Name)) #Printing the damage dealt
    elif RandomN == 1:
     Fighter1.Health = Fighter1.Health-Fighter2.AvgAttackDamage
     Fighter2.Health = Fighter2.Health-Fighter1.AvgAttackDamage-5 #Making fighter 1 stronger
     print(str(Fighter1.Name) + " dealt " + str(Fighter1.AvgAttackDamage-5) + " damage to " + str(Fighter2.Name))#Printing the damage dealt
     print(str(Fighter2.Name) + " dealt " + str(Fighter2.AvgAttackDamage) + " damage to " + str(Fighter1.Name))#Printing the damage dealt
    elif RandomN == 2:
       Fighter1.Health = Fighter1.Health-Fighter2.AvgAttackDamage
       print("Fighter 2 took no damage") #Printing the damage dealt
       print("Fighter 1 lost " + str(Fighter2.AvgAttackDamage) + " health") #Printing the damage dealt
       #Taking no damage from Fighter 2 DEFENSE MODE
       
    elif RandomN == 3:
       Fighter2.Health = Fighter2.Health-Fighter1.AvgAttackDamage
       print("Fighter 1 took no damage")
       print("Fighter 2 lost " + str(Fighter1.AvgAttackDamage) + " health")
       #Taking no damage from Fighter 1 DEEFNSE MODE
    if Fighter1.Health <=0:
        print(Fighter1.Name + " has died.") #Showing that fighter one has died
        Fighter1.Health = 100
    if Fighter2.Health <=0:
        Fighter2.Deaths = Fighter2.Deaths + 1
        print(Fighter2.Name + " has died.") #Showing that fighter two has died
        Fighter2.Health = 100

while loopCount<100 and Man1.Health > 0 and Man2.Health > 0: #Checking that they are alive and making them stop fighting after 100 rounds
   print("Round " + str(loopCount+1) + " has begun!")
   Fight(Man1,Man2) #Getting both of the people to fight
   loopCount = loopCount + 1
print("Yug has died " + str(Man2.Deaths) + " times") #Printing the amount of deaths
print("Tom has died " + str(Man1.Deaths) + " times") #Printing the amount of deaths