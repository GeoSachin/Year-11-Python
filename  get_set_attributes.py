class Pet:
    def __init__(self, name, category, breed = None, age = 0): #Defining the class (Pet)
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

def get_weight(self): #This is the function that gets the weight of the object in the class (Pet)
        return(self._name + " has a weight of " + str(self.weight) + "kg.")
def set_weight(self, WeightToSet): #This function sets the weight of the object in the class
        if type(WeightToSet) == int or type(WeightToSet) == float: #Checking that the weight is a number
            if WeightToSet > 0: #Checking that the weight is positive
                self.weight = WeightToSet
                return("The weight of " + self._name + " has been set to " + str(WeightToSet) + "kg." )
            else:
                return("Please enter a valid weight that is greater than 0 and numerical.")

Pet1 = Pet("Tom", "Dog", "German Shepherd", 4)
Pet2 = Pet("Ron", "Cat", "Chiwawa", 3) #Defining two pets

WeightForTom = int(input("what is the weight of Tom? "))
WeightForRon = int(input("what is the weight of Ron? ")) #Receiving the input on what the weights are

set_weight(Pet1, WeightForTom)
set_weight(Pet2, WeightForRon) #Setting the weight for the two pets

print(get_weight(Pet1))
print(get_weight(Pet2)) #Printing the weights of the two pets
