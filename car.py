class Car: #Create a class named Car
    def __init__(self, model, year, engine): #Define the constructor with parameters model, year, and engine
        self.model = model
        self.year = year
        self.engine = engine
Car1 = Car("Toyota", 2020, "V6") #Create an instance of the Car class
Car2 = Car("Honda", 2019, "V4")
Car3 = Car("Ford", 2021, "V8")
Car4 = Car("Chevrolet", 2018, "V6")
Car5 = Car("Nissan", 2022, "V4")

for i in [Car1, Car2, Car3, Car4, Car5]: #Looping through a list of all the cars to print through the attributes of each car
    print(f"Model: {i.model}, Year: {i.year}, Engine: {i.engine}")