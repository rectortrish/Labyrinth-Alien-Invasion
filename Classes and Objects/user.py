
class User:
    def __init__ (self, first_name, last_name, username,email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location

        self.login_attempts = 0

    def describe_user(self):
        print (f"{self.first_name} {self.last_name}")
        print (f" Username: {self.username}")
        print (f" Email: {self.email}")
        print (f" Location: {self.location}")

    def greet_user(self):
        print (f"Welcome back, {self.username}")


    def increment_login_attempts(self):
        #Increment the value of login_attempts by 1
        self.login_attempts +=  1

    def reset_login_attempts (self):
        #Reset login attempts to 0
        self.login_attempts = 0


        

mrs_rector = User ("Trish", "Rector", "t_rector", "t_rector@example.com", "Sammamish")
mrs_rector.describe_user()
mrs_rector.greet_user()


print ("Making 3 login attempts")

mrs_rector.increment_login_attempts()
mrs_rector.increment_login_attempts()
mrs_rector.increment_login_attempts()

print (f" Login attempts: {mrs_rector.login_attempts}")


print ("Resetting login attempts...")
mrs_rector.reset_login_attempts()

print (f" Login attempts: {mrs_rector.login_attempts}")
        
               

        
