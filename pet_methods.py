class Pet:
    def __init__(self, name, category, age = 0): #The class has been defined for the Pets that are going to be made
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = 0
    
    def have_birthday(self):
        self.age += 1
def vaccinate(pet): #This is the function that can remotely vaccinate pets by inserting a parameter
    pet.vaccinated = True
    if pet.vaccinated == True:
     return(pet.name + " has ben vaccinated!")
    else:
       return("Error in vaccinating " + Pet.pet.name)

def clear_balance(pet): #This function goes into the attributes of the class 'Pet' and changes the account balance to 0. If there is an error, it prints it out.
    pet.account_balance = 0
    if pet.account_balance == 0:
       return(pet.name + " has $0 in their account")
    else:
       return("Unable to clear the balance in " + Pet.pet.name + "'s account. They have $" + str(Pet.pet.account_balance) + " remaining.")
def HumanAge(pet): #This function calculates the human age of the pet if it is a cat or a dog. If it is neither, it states that it can not calculate it.
   if pet.category == "Cat":
      Humanage = pet.age*6
      return(Humanage)
   elif pet.category == "Dog":
       Humanage = pet.age*7
       return(Humanage)
   else:
      return("As the pet is neither a dog nor a cat, we can not determine its human age.")

Pet1 = Pet("Tom", "Cat", 2)
Pet1.account_balance = 23
Pet1.ccard = "3121 2183 3213 8934"
Pet2 = Pet("Ron", "Dog", 4)
Pet2.account_balance = 4
Pet3 = Pet("Sam", "Bird", 1)
Pet3.account_balance = 1
#These lines define 3 different pets. The bird was added to test whether or not it will work to calculate human age if it not a car nor a dog.

print(vaccinate(Pet1))
print(clear_balance(Pet1))
print(HumanAge(Pet1))
print(vaccinate(Pet2))
print(clear_balance(Pet2))
print(HumanAge(Pet2))
print(vaccinate(Pet3))
print(clear_balance(Pet3))
print(HumanAge(Pet3))
#These lines print out the function which will print the returned value when the functions were defined.