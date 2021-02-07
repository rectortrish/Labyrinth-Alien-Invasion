#How to change an attribute directly and how to change it in a method.

class Restaurant:
    def __init__ (self, name, cuisine_type):
        
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0 #add an attribute called number_served

    def describe_restaurant (self):
        print (f"{self.name} serves delicious {self.cuisine_type}")

    def open_restaurant (self):
        print (f"{self.name} is now open")

    def set_number_served (self, number_served): #method to set customers served
        self.number_served = number_served
        print (f"{self.name} has served {self.number_served} customers today.")

    def increment_number_served (self, additional_customers):
        self.number_served += additional_customers
        print (f"{self.name} has served {self.number_served} customers today.")


mcdonalds = Restaurant ("McDonald's", "hamburgers")
mcdonalds.describe_restaurant()

print (mcdonalds.number_served) #using an attribute to print number of customers served




mcdonalds.set_number_served (600) #using a method to print number of customers served
mcdonalds.increment_number_served(43) #using a method to increment number of customers served 





