# def creat_cubes(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result

# print(creat_cubes(10))


def creat_cubes(n):

    for x in range(n):
        yield x**3

# for x in creat_cubes(10):
#     print(x)
print(list(creat_cubes(10)))

def gen_fibo(n):

    a = 1
    b = 1
    #output = []
    for i in range(n):
        #output.append(a)  this is not memory efficent , use yield can improve the memory efficency
        yield a
        a,b = b,a+b

for number in gen_fibo(10):
    print(number)


def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
print(next(g))
print(next(g))


s = 'hello'
for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))



