
# Electric Car Inheritance Example

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        self.odometer_reading = 0     #setting a default value for an attribute

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def fill_gas_tank(self):
        print (f"This car takes 20 gallons of gas.")


class Battery:
    def __init__ (self, battery_size = 75):
        self.battery_size = 75
        
    def describe_battery(self):
        print (f"This lovely car has a {self.battery_size} - KWh battery.")


        
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print ("This car doesn't need a gas tank!")
        
        

my_new_car = Car ("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())


my_tesla = ElectricCar ("tesla", "model s", 2019)
print (my_tesla.get_descriptive_name())
#my_tesla.describe_battery()
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
