import math
# '''
# this is OOP in python with udemy
# '''
# class Dog():
#     #class object attribute
#     #same for any instance of a class
#     species = 'mammal'


#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
    
#     def bark(self):
#         print('WOOF! My name is {}'.format(self.name))
    
# my_dog = Dog(breed="Husky", name='Sally')
# print(my_dog.bark())


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
        return self.pi*self.radius*self.radius*self.height
        

    def surface_area(self):
        return self.pi*2*self.radius*self.height + self.pi*2*self.radius*self.radius
       

c = Cylinder(2, 3)

print(c.volume())
print(c.surface_area())


'''
 EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
In [3]:
li.distance()
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
        return sqrt((self.coor1[0]-self.coor2[0])**2 + (self.coor1[1]-self.coor2[1]**2)

#coordinate2=(8, 10)
#li=Line(coordinate1, coordinate2)
#li.distance()

coordinate1 = (2, 3)
coordinate2 = (8, 10)
li=Line(coordinate1, coordinate2)

