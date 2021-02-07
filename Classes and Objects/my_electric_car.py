#Using multiple classes from a module

from electric_car import ElectricCar

my_tesla = ElectricCar ("tesla", "model s", 2919)

print (my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()

