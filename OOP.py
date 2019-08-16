import math
'''
this is OOP in python with udemy
'''
class Dog():
    #class object attribute
    #same for any instance of a class
    species = 'mammal'


    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    
    def bark(self):
        print('WOOF! My name is {}'.format(self.name))
    
my_dog = Dog(breed="Husky", name='Sally')
print(my_dog.bark())


class Circle():

    #CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):

        self.radius = radius

    #Method
    def get_circumference(self):
        return self.radius * self.pi *2
   
my_circle = Circle(30)
print(my_circle.get_circumference())


        


class Animal():
    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')
    
    def eat(self):
        print('I am eating')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
    
    def who_am_i(self):
        print('I am a dog')

mydog = Dog()
mydog.eat()
mydog.who_am_i()


class Book():

    def __init__(self, tittle, author_name, pages):
        
        self.tittle = tittle
        self.author_name = author_name
        self.pages = pages

    def __str__(self):
        return(f"{self.tittle} by {self.author_name}")

    def __len__(self):
        return self.pages
b = Book('An intro to Java', 'Walter', 350)

print(b)
print(len(b))


'''OOP homework'''

'''
# EXAMPLE OUTPUT
c = Cylinder(2,3)
In [7]:
c.volume()
Out[7]:
56.52
In [8]:
c.surface_area()
Out[8]:
94.2
'''

class Cylinder:

    pi = 3.14
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi*(self.radius)**2 *self.height
        

    def surface_area(self):
        return self.pi*2*self.radius*self.height + self.pi*2*(self.radius)**2

c = Cylinder(2, 3)

print(c.volume())
print(c.surface_area())


'''
 EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)
Out[3]:
9.433981132056603
In [4]:
li.slope()
Out[4]:
1.6
'''

class Line:
   
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return math.sqrt((self.coor1[0]-self.coor2[0])**2 + (self.coor1[1]-self.coor2[1])**2)
    
    def slope(self):
        return (self.coor2[1]-self.coor1[1]) / (self.coor2[0]-self.coor1[0])


point1 = (3,2)
point2 = (8,10)
li=Line(point1, point2)
print('The distance is {}'.format(li.distance()))
print('The slope is {}'.format(li.slope()))

'''
simple example of class
'''

class Simple:
    def __init__(self, amount):
        self.amount = amount
    def add_amount(self, deposit):
        self.amount = self.amount + deposit

myAcct = Simple(200)
print(myAcct.amount)
myAcct.add_amount(300)
print(myAcct.amount)

'''
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''
class BankAcct:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print('Account Owner is {}'.format(self.owner))
        print('Account Balance is {}'.format(self.balance))

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Deposit Accepted {amount}')
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance >= 0:
            print(f'Withdrawal Accepted {amount}')
        else:
            print('Funds Unavailable!') 


person1 = BankAcct('Sally', 200)
print(person1.owner)
print(person1.balance)
person1.deposit(100)
print(person1.balance)
person1.withdraw(50)
print(person1.balance)
person1.withdraw(400)
print(person1.balance)