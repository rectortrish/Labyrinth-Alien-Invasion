

class Restaurant:
    def __init__ (self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant (self):
        print (f"{self.name} serves delicious {self.cuisine_type}")

    def open_restaurant (self):
        print (f"{self.name} is now open")


mcdonalds = Restaurant ("McDonald's", "hamburgers")
mcdonalds.describe_restaurant()

taco_time = Restaurant ("Taco Time", "tacos")
taco_time.describe_restaurant()

dairy_queen = Restaurant ("Dairy Queen", "Sundaes")
dairy_queen.describe_restaurant()

