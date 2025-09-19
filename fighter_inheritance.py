import random, time 

class Fighter: #Creating a fighter class
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self): #Checks if the character is dead
        if self.__health <= 0:
            return True
        else:
            return False #This prints the value of the function after it is done

    def random_attack(self): #Randomly attacks a character
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        print('Attack power:', attack_power) #Printing the attack power of the character
        print(self.magic + " is the magic of " + self.name) #Printing the magic of the Wizard, Yug
        return attack_power #This value will be returned by the function so whenever the function is called and the value is equal to a variable, this return value will be equal to the value of the variiable

    def skill_attack(self): #Innitiates the skill attack at a random given time
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        target = random.randint(2,6)
        print('Hit enter in exactly',target,'seconds') #Timing the attack
        tic = time.time()
        input()
        toc = time.time() 
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 2: #Checks by how mucht the attack is bring multiplied by
            multiplier = 0 #If the multiplier is too small, it is automatically set to 0

        print('Attack power:', attack_power) #Printing out the attack power of the character
        print('Multiplier:', multiplier) #Printing out the attack multiplier of the character
        return attack_power*multiplier

    def defend(self,attack_power):#A function used to defend a character
        damage = attack_power - self.shield
        if damage >  0: #Checking if there is any damage which is positive
            self.__health -= damage #Taking damage from the character
            print('Damage:', damage) #If tehre is damage, it prints that
        else:
            print('No damage') #Either there is no damage or negative damage, which makes no sense so it takes no damage and prints that

Wizard = Fighter("Yug", 500, "Staff", False) #Creating a fighter that is a Wizard called Yug
Wizard.magic = "Disappear" #Adds a magic for the wizard that makes their opponent disappear  instantly


