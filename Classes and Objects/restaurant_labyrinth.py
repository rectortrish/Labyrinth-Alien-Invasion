#Homework 9-4 pg. 167
#Number served

class Restaurant:
    def __init__ (self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant (self):
        print (f"{self.name} serves yummy {self.cuisine_type}")

    def open_restaurant (self):
        print (f"{self.name} is now open. Come on in.")

    def set_number_served (self, number_served):
        self.number_served = number_served

    def increment_number_served (self, additional_served):
        self.number_served += additional_served


        
restaurant = Restaurant ("Mcdonald", "junk food")
print (restaurant.number_served)

restaurant.describe_restaurant()

restaurant.set_number_served (589)
print (f"Number served: {restaurant.number_served}")

restaurant.increment_number_served (6759)
print (f"New number served: {restaurant.number_served}.")



#Homework due 1/13

#Please do 9-3 on page 162 and 9-5 on page 167, "Login attempts"
