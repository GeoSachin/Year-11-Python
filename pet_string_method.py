class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False #Setting the default values for the pets

    def __str__(self): #Creating the function that your class will use to print the details of the pets
        if self.ccard != 'unknown':
            card_details = str(self.name + ' is a ' + str(self.age) + ' year old ' + self.category + ' with a credit card number of ' + str(self.ccard))
            return(card_details)
        else:
            return(self.name + ' is a ' + str(self.age) + ' year old ' + self.category + ' with no credit card number')
        if self.vaccinated:
            return(self.name + ' is vaccinated')
        else:
            return(self.name + ' is not vaccinated')

Cat = Pet('Fluffy', 'cat', 3)
Dog = Pet('Rover', 'dog', 5)
Worm = Pet('Wiggles', 'worm', 1)
Fish = Pet('Bubbles', 'fish', 2)
Bird = Pet('Tweety', 'bird', 1)
Dog.ccard = '1234-5678-9012-3456'
Bird.ccard = '9876-5432-1098-7654'
Dog.vaccinated = True
Bird.vaccinated = True #Setting all of the details of the pets

print(Cat)
print(Dog)
print(Worm)
print(Fish)
print(Bird)
#Printing all of the details of the pets