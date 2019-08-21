'''
Create a generator that generates the squares of numbers up to some number N.
'''

import random


def gensquare(N):
    for number in range(N):
        yield number**2

for x in gensquare(10):
    print(x)

'''
Create a generator that yields "n" random numbers between a low and high number (that are inputs). 
'''


def rand_num(low, high, n):
    
    for number in range(n):
        number = random.randint(low, high)
        yield number 


for num in rand_num(1,10,12):
    print(num)


'''
Use the iter() function to convert the string below into an iterator:
'''
s = 'hello'

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))


    

