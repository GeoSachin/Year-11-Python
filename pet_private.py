class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category #Category is now a private element and can not be changed (the __ indicates that)
        self.__breed = breed #The breed is now a private attribute.
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
# Creation of the class
    def have_birthday(self): #Increases the age of the pet by 1.
        self.age += 1

    def __str__(self): #This notation is used to print out the class as a string def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19: #Checks if the credit card input is a valid credit card and meets the numerical criteria 
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + "\nBreed: " + str(self.__breed) + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status #This is used to split the values into seperate lines and print it

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10, breed= "Siamese")
p1.__category = "Dog" #Checking whether it is possible to change the category from cat to dog even though it was private.
p1.__breed = "Chiwawa" #Checking whether it is possible to change the breed even though it was private.
print(p1) #The category and breed was not changed, proving that it is private.
