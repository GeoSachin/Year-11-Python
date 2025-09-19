class Pet: #Defining a class called Pet
    def __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age
        self.vaccinated = False
        self.ccard = "unknown"
        self.billing_address = "unknown"
        self.owner_name = "unknown"
        self.account_balance = 0.0

p1 = Pet("Bonnie", "Cat", 3) #Creating an object of the class Pet
p1.vaccinated = True
p1.ccard = "3423 2326 7543 1234"
p1.billing_address = "17 Park Drive, The Shire 2695"
p1.owner_name = "Alex Ngyuen"
p1.account_balance = 129.95 #Assigning values to the attributes of the object
p2 = Pet("Fox", "Dog", 4) #Creating an object of the class Pet
p2.vaccinated = False
p2.ccard = "1234 5678 9012 3456"
p2.billing_address = "1234 Elm Street, Springfield 1234"
p2.owner_name = "John Doe"
p2.account_balance = 0.0 #Assigning values to the attributes of the object

if p1.vaccinated == True:
    print("Bonnie has been Vaccinated")
else:
    print("Bonnie has not been Vaccinated") #Printing vaccination status of the cat
print("Bonnie is " + str(p1.age) + " years old") #Printing the age of the cat
print("Bonnie's owner is " + p1.owner_name) #Printing the name of the owner of the cat
print("Bonnie's billing address is " + p1.billing_address) #Printing the billing address of the owner of the cat