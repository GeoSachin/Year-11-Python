class Pet: #Creation of the class
    def __init__(self, name, category, age = 0): #Parameters added to the class
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False #Adding attributed to the class
    def __str__(self): #Using string method so that the class can be printed later onwards
        if self.vaccinated == True:
            return(self.name + " has been vaccinated.")
        else:
            return(self.name + " has not been vaccinated.")


Pet1 = Pet("Shahwat", "Dog", 4)
Pet2 = Pet("Yug", "Cat", 2)
Pet3 = Pet("Sam", "Cat", 3)
Pet4 = Pet("Tom","Fish", 1)
Pet5 = Pet("Aaron", "Cow", 12)
Pet6 = Pet("Bob", "Bird", 4) # Created different types of pets
Pets = [Pet1, Pet2, Pet3, Pet4, Pet5, Pet6] # Added all of the pets created into a list so that we can loop through the list to change all of the pets' attributes

for pet in Pets:
    pet.vaccinated = True #Looping through the list and vaccinating all the pets
    print(pet) #Printing the vaccination of each pet AFTER vaccinating it