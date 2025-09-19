import random
import time
skillBuff = 1.3 #The amount the attack will be multiplied by if it is a skill attack
class Fighter:
    def __init__(self, name, health, weapon, shield):
        self.name = name
        self.__health = health
        self.weapon = weapon
        self.shield = shield

    def weapon_selection(self): #chooses a weapon
        choiceweapon = input("Select a weapon: Sword, Axe, Mace: ")
        choiceweapon = choiceweapon.capitalize()

        if choiceweapon == 'Sword': #if statement which selects weapon based on user input, changing the weapon variable
            self.weapon = 50
        elif choiceweapon == 'Axe':
            self.weapon = 60
        elif choiceweapon == 'Mace':
            self.weapon = 40
        else:
            while choiceweapon != ['Sword', 'Axe', 'Mace']:
                print("Please choice a valid weapon")
                choiceweapon = input("Select a weapon: Sword, Axe, Mace: ") #while loop to ensure weapon is chosen

        print(f"You have chosen the might {choiceweapon}, it's strength is {self.weapon}")

    def shield_selection(self): #chooses a shield
        print()
        choice_cave = input(f"While testing your weapon, you stumble into the entrance of a cave! Do you dare to enter? Reply 'Yes' or 'No': ") #added story
        if choice_cave == 'No': #if loop depending on user selection
            self.shield = 20
            print("The cave's mysteries will forever be unknown")
        elif choice_cave == 'Yes':
            self.shield = 50
            print("The luck was in your favour today, you have found a brand new shield!")
        else:
            while choice_cave != ['Yes', 'No']: #while loop to ensure a choice
                print("Please reply with Yes or No")
                choice_cave = input("Yes or No?: ")

    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2*skillBuff), int(self.weapon*2)) #range of the weapon
        print(f"Attack power: {attack_power}")
        return attack_power

    def defend(self, attack_power): #damage function which subtracts attack power from the shield
        damage = attack_power - self.shield #damage calculation
        if damage > 0: #calculates if the damage or the shield was stronger, if damage stronger: damage is removed from health otherwise nothing happens
            self.__health -= damage
            print(f"Damage: {damage}")
        else:
            print(f"No Damage!")

    def get_health(self): #getter to access privatised health attribute
        return self.__health

    def fight_to_death(self): #loop to simulate a fight

        print(f"You: {you.get_health()}")
        time.sleep(0.5) #readability
        print(f"Opps: {opps.get_health()}")
        time.sleep(0.5)
        print()

        while you.get_health() > 0 and opps.get_health() > 0: #while loop which runs while health is positive integers
            print("You attack the opposition")
            attack_power = you.random_attack() #runs attack power function
            opps.defend(attack_power) #calculates real damage on player
            print(f"Opps Health: {opps.get_health()}")
            print()
            time.sleep(0.5)

            if opps.get_health() <= 0:
                break

            print("The opposition attacks you . . .") #same thing as the first one, just reversed for opps damaging you (player)
            attack_power = opps.random_attack()
            you.defend(attack_power)
            print(f"Your Health: {you.get_health()}")
            print()
            time.sleep(0.5)

        if you.get_health() > opps.get_health(): #once someone's health reaches zero, this comparison operator checks whom's health is higher and awards the title
            print("You are the mighty champion!")
        elif you.get_health() < opps.get_health():
            print("The opps have won!")
        else: #just in case
            print("Stalemate")


you = Fighter("You", 200, 50, 4)
opps = Fighter("Gladiator", 200, 50, 4)

you.weapon_selection()
you.shield_selection()
you.fight_to_death()
