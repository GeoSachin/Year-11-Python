#---begin Python ---
class Car:
    def __init__(self, make, model, year, colour): #The syntax used to create a class
        self.make = make #The brand of the car
        self.model = model #The type of brand of the car
        self.year = year #The year the car was manufactured
        self.colour = colour #The visual description of the car based on its colour
    
    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

# Instantiating objects from the Car class
car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("Honda", "Civic", 2018, "Blue")

car1.start()  # Output: Toyota Camry is starting.
car2.stop()   # Output: Honda Civic is stopping.
#--- end python ---
