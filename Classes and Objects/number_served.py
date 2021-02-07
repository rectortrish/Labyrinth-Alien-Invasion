

class Restaurant:
    def __init__ (self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant (self):
        print (f"{self.name} serves delicious {self.cuisine_type}")

    def open_restaurant (self):
        print (f"{self.name} is now open")

    def set_number_served (self, number_served):
        self.number_served = number_served

    def increment_number_served (self, additional_served):
        self.number_served += additional_served
    

restaurant = Restaurant ("Dominos", "pizza")
print(restaurant.number_served) #using attribute 
restaurant.set_number_served(58764) #using method
print(restaurant.number_served)

restaurant.increment_number_served (495)
print(f" Number served: {restaurant.number_served}")


'''restaurant.number_served = 367
print(restaurant.number_served)'''


mcdonalds = Restaurant ("McDonald's", "hamburgers")
mcdonalds.describe_restaurant()

taco_time = Restaurant ("Taco Time", "tacos")
taco_time.describe_restaurant()

dairy_queen = Restaurant ("Dairy Queen", "Sundaes")
dairy_queen.describe_restaurant()

