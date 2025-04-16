"""

##############################################

for i in range(5):
    print(i)  # prints 0 to 4

##############################################
    x = 0
while x < 5:
    print(x)
    x += 1
##############################################
"""
def greet(name):
    return f"Hello, {name}!"

#print(greet("Ali"))


##############################################
def order_pizza(*toppings):
    for topping in toppings:
        print(f"Adding {topping} to your pizza")

#order_pizza("cheese", "pepperoni", "olives")
##############################################
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#print_info(name="Ali", age=20, city="Amman")
##############################################

def register_user(**details):
    print("User registered with:")
    for field, info in details.items():
        print(f"{field} = {info}")

#register_user(name="Nour", email="nour@example.com", password="1234")
##############################################

"""print("Hello", end='')  # no new line
print(" World")
print (float(1))
"""

class Car:
    def drive(self):
        print("Driving the car")

# Create object
my_car = Car()
my_car.drive()  # Output: Driving the car

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I’m {self.name} and I’m {self.age} years old."

p = Person("Ali", 22)
print(p.greet())



class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound1(self):
        return "Bark"
    

class BankAccount :
    def __init__(self, UserInput):
        self.__Balance = UserInput

    def deposit (self,UserInput):
        self.__Balance += UserInput

    def GetBalance(self):
        print(f"Your balance now is : {self.__Balance}")


Person1 = BankAccount(2500)
Person1.deposit(270)
Person1.GetBalance()            

my_list = [1, 2, 3, 2, 4]
print(my_list[0])         # Access element
print(0 in my_list)       # Check membership

class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):  # 👈 looks like a variable
        return self.__age

    @age.setter
    def age(self, value):  # 👈 you control what happens when it's set
        if value >= 0:
            self.__age = value
        else:
            raise ValueError("Age must be positive")

p = Person()
p.age = 25         # ✅ works
print(p.age)       # ✅ works
#p.age = -5         # ❌ raises error
