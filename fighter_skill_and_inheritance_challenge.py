import random, time 
print("You enter a cave and you see a wizard, the wizard wants to attack you, what do you do??") #Story beginning
class Fighter: #The fighter class that can be replicated to create different fighters
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
        
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self):
        if self.__health <= 0: #Checks if the health is negative or 0 to find if it is alive or dead
            return True
        else:
            return False

    def random_attack(self): #A random attack function that can be called to take damage from the other character
        attack_power = random.randint(5,10)
        print('Attack power:', attack_power)
        return attack_power

    def skill_attack(self): #A skill attack function with a higher attack power
        attack_power = random.randint(20,25)
        target = random.randint(1,2)
        print('Hit enter in exactly',target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 2: 
            multiplier = 0

        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier

    def defend(self,attack_power): #A method to defend oneself
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')


class Wizard(Fighter): #Creating a wizard class
    def __init__(self,name, starting_health, weapon, shield,magic):
        super().__init__(name, starting_health, weapon, shield)
        self.magic = magic

    def random_attack(self):
        attack_power = random.randint(5, 10)
        print('Attack power:', attack_power)
        return attack_power + self.magic


you = Fighter('You',100,10,20)
wiz = Wizard('The Grey Wizard',200,20,10,30)

you.report()
wiz.report()

while True: #The loop that ensures that the game continues, this loop makes the game more engaging
    print('You attack the',wiz.name)
    wiz.defend(you.skill_attack())
    wiz.report()
    time.sleep(2)
    print('')
    if wiz.is_dead():
        print('You win')
        break
    print(wiz.name,'attacks you . . .')
    you.defend(wiz.random_attack())
    you.report()
    time.sleep(2)
    if you.is_dead():
        print(wiz.name,'wins')
        break
    print('')
