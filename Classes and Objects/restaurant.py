# Homework 9-6, page 173, IceCream Stand
# Working with inheritance


class Restaurant:
    def __init__ (self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 69

    def describe_restaurant (self):
        print (f"{self.name} serves delicious {self.cuisine_type}")

    def open_restaurant (self):
        print (f"{self.name} is now open")

    def set_number_served (self, number_served):
        self.number_served = number_served
        print (f"{self.name} had served {self.number_served} customers today.")

    def increment_number_served (self, additional_served):
        self.number_served += additional_served
        print (f"{self.name} had served {self.number_served} customers today.")

class IceCreamStand (Restaurant):
    def __init__ (self, name, cuisine_type = "Ice Cream"):
        super().__init__ (name, cuisine_type)
        self.flavors = []

    def show_flavors (self):
        print (f"We have the following delicious flavors available:")
        for flavor in self.flavors:
            print (f" - {flavor.title()}")


big_one= IceCreamStand("The Big One")

big_one.flavors = ["vanilla", "rocky road", "peach", "black cherry"]

big_one.describe_restaurant()
big_one.show_flavors()
                   
                   
    








