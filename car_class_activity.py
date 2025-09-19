class Car: #Creating the class
    def __init__(self,make,model,year,price=None): #Defining the parameters for the class
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self): #Using string method to allow for printing of the class later onwards
        if self.year>2010:
            self.sale = True #Setting sale to true if the car is a 2010+ model
            return(self.make + "is a " +str(self.year) + " car that is for sale")
        else:
            self.sale = False #Setting sale to false if the car is a 2010- model
            return(self.make + "is a " +str(self.year) + " car that is not for sale")

c1 = Car('Mazda','6',2005)
c2 = Car('Toyota', "Camry", 2018)
c3 = Car("Toyota", "Echo", 2002)
c4 = Car("Ford", "Falcon", 2011)
#Defining different types of cars

cars = [c1,c2,c3,c4] #Adding the cars to the list

for car in cars:
    print(car) #Printing the sale status of each car