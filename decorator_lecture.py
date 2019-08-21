'''
this is a decorator example
'''


def hello(name='Sally'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello'

    #print(greet())

    def welcome():
        return '\t This is welcome() inside hello.'

   # print(welcome())

    print('I am going to return a func')

    if name == 'Sally':
       return greet
    else:
       return welcome


my_new_func = hello('Sally')

#
# def cool():
#
#     def super_cool():
#         return 'I am very cool!'
#
#     return super_cool()


def hello():
    return 'Hi Sally!'


def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())


other(hello)


def new_decorator(original_func):

    def wrap_func():

        print('Some extra code')

        original_func()

        print('Some extra code, after the original function')

    return wrap_func


# def func_needs_decorator():
#     print('I want to be decorated!')


# func_needs_decorator()
#
# decorated_func = new_decorator(func_needs_decorator)
#
# decorated_func()

@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')


func_needs_decorator()


