class Pet: #Defining the class pet
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

def set_name(self,new_name): #Setting the name of the pet
        if type(new_name) == str:
            self._name = new_name
        else:
            print('Please use a string as a name attribute') #Highlights the error if it does not work
    
def get_name(self): #Getting the name of the pet
        return self._name

def get_weight(self):
        return self.weight

def get_category(self):
        return self.__category
    
def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float: #Checks if it is valid
            if new_weight > 0: #Checks if the new weight is positive
                self.weight = new_weight
            else:
                print('Please enter a positive number for weight')
        else:
            print('Please enter a number for weight')

def __str__(self):
        payment_status = 'unregistered'
        my_status = 'Name: ' + self._name + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name='Bonnie', category='Dog')
p2 = Pet('Clyde','Cat','Persian',12)
p3 = Pet('Cindy', 'Dog',age = 3)
p4 = Pet("Yug,", "Dog", age=4)
p5 = Pet("Shashwat", "Turtle", age=2) #Creates 5 pets
set_weight(p5, 5)
set_weight(p4, 700)
set_weight(p3, 1)
set_weight(p2, 6)
set_weight(p1, 2) #Sets the weight for the 5 pets

pets = [p1,p2,p3] 
pets.append(p4)
pets.append(p5) #Puts all of the pets in a list
for i in pets:
    currentWeight = get_weight(i)
    set_weight(i, currentWeight+1)#Increases all of the weights of the pets by 1
for i in pets:
      print(i._name + " has a weight of " + str(get_weight(i)) + "kg.") #Prints the weight of all of the pets

dogs = pets
dogs.remove(p2)
dogs.remove(p5) #Removes all of the pets that are not dogs

for i in dogs:
            print(__str__(i)) #Prints the details of only the dogs
