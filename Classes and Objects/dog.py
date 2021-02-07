
# A simple class to model a dog


class Dog:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def sit (self):
        print (f"{self.name} is now sitting.")
        #print (f"{self.name} is {self.age} years old.")

    def roll_over(self):
        print (f"{self.name} just rolled over.")


#Creating an instance        

my_dog = Dog ("Daisy", 12)
your_dog = Dog ("Booda", 10)



#Accessing attributes

print(my_dog.name)
print(my_dog.age)

print (f"My dog's name is {my_dog.name}.")

print (f"Your dog's name is  {your_dog.name}.")

print (f"{my_dog.name} is {my_dog.age} years old.")

print (f"{your_dog.name} is {your_dog.age} years old.")


#Calling methods

my_dog.sit()
my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()

