'''LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
 but returns the greater if one or both numbers are odd¶
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5'''


def lesser(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 < num2:
            return num1
        else:
            return num2
    else:
        if num1 < num2:
            return num2
        else:
            return num1


print(lesser(2, 4))
print(lesser(2, 5))

'''ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False'''


def animal_crackers(my_string):
    new_list = my_string.split(" ")
    print(new_list)
    return new_list[0][0] == new_list[1][0]


print(animal_crackers('Levelheaded Llama'))
assert animal_crackers('Crazy Kangaroo') == False
print('All pass')


'''MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
or if one of the integers is 20. If not, return False¶
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False'''


def makes_twenty(num1, num2):
    if num1 == 20 or num2 == 20:
        return True
    else:
        return num1 + num2 == 20


assert makes_twenty(20, 10) == True
assert makes_twenty(12, 8) == True
assert makes_twenty(2, 3) == False

print('all pass')

'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
e.g: ('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'
'''


def old_mcdonald(name):
    new_name = name[0].upper() + name[1:3] + name[3].upper() + name[4::]
    return new_name


assert old_mcdonald('macdonald') == 'MacDonald'
print('Test passed')


def rotateString(s, offset):
    # write your code here
    if offset == 0:
        return s
    else:
        cut_position = len(s)-offset
        new_string = s[cut_position::] + s[0:cut_position]
        return new_string


print(rotateString("abcdefg", 3))


def deduplication(nums):
    # write your code here
    # index = 0
    # count = 1
    # new_nums = nums.sort()
    # while count < len(nums):
    #     if new_nums[index] != new_nums[count]:
    #         index += 1
    #     else:
    #         count += 1

    # return count
    return len(set(nums))


print(deduplication([1, 2, 3, 1, 2, 4]))

print('abd,oui,jgsv,.'.strip(',.'))


'''
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list 
with some connector string. For example, some uses of the .join() method:

>>> "--".join(['a','b','c'])
>>> 'a--b--c'

This means if you had a list of words you wanted to turn back into a sentence, 
you could just join them with a single space string:

>>> " ".join(['Hello','world'])
>>> "Hello world"

'''


def master_yoda(text):
    temp_list = text.split()[::-1]
    print(temp_list)
    return " ".join(temp_list)


assert master_yoda('I am home') == 'home am I'
print('test pass')

'''
Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True

NOTE: abs(num) returns the absolute value of a number
'''


def almost_there(num):
    if num <= 0:
        return False
    else:
        temp_num1 = num - 100
        temp_num2 = num - 200
        if abs(temp_num1) <= 10 or abs(temp_num2) <= 10:
            return True


assert almost_there(104) == True
assert almost_there(209) == True
assert almost_there(-1) == False
assert almost_there(205) == True
assert almost_there(198) == True

print('almost_there test pass')

'''
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''


def has_33(my_list):
    i = 0
    j = 1
    if len(my_list) == 0:
        return False
    while i < j:
        if my_list[i] != 3:
            i += 1
            j += 1
            if my_list[i] == my_list[j]:
                return True
        return False


assert has_33([]) == False
assert has_33([1, 3, 1, 3]) == False
assert has_33([1, 3, 3]) == True
assert has_33([3, 1, 3]) == False
print('has_33 test pass')

'''

PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

'''


def paper_doll(myString):
    return ''.join([x*3 for x in myString])


print(paper_doll("myhello"))

'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, 
return 'BUST'¶
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''


def blackjack(num1, num2, num3):
    sum = num1 + num2 + num3
    if 0 < num1 < 12 and 0 < num2 < 12 and 0 < num3 < 12:
        if sum <= 21:
            return sum
        else:
            if num1 == 11 or num2 == 11 or num3 == 11:
                return sum-10
            else:
                return ('BUST')
    else:
        return ('choose a num between 1 and 11')


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
print(blackjack(12, 1, 2))


'''

SUMMER OF '69: Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
Return 0 for no numbers.¶
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
'''
# def summer_69(myList):
#     i = 0
#     j = 1
#     newList = []
#     for i in range(len(myList)):
#         if myList[i] != 6:
#             newList.append(myList[i])
#             i += 1
#             j += 1
#         else:
#             for j in range(len(myList)):
#                 if myList[j] != 9:
#                     j+=1
#                 else:
#                     newList.append(myList[j+1])

#         print(newList)
#         return sum(newList)


def summer_69(nums):
    flag = False
    sum = 0

    for num in nums:
        if(num == 6):  # Turn the flag on if the number is 6
            flag = True
            continue
        if(num == 9 and flag is True):  # Turn the flag Off when 7 is seen after 6
            flag = False
            continue
        if(flag is False):  # Keep on adding the nums otherwise
            sum += num
    return sum


print(summer_69([1, 3, 5]))
print(summer_69([2, 1, 6, 9, 11]))

'''

SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order¶
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False

'''

# def spy_game(my_list):
#     flag = False
#     for num in my_list:
#         if num == 0:
#             flag = True
#             continue
#         if num == 7 and flag = True:
#             flag = false
            

def find_11(nums):
    flag = False

    for num in nums:
        if(num == 1):  # Turn the flag on if the number is 1
            flag = True
            continue
        if(num == 1 and flag is True):  
            return ('has 1,1 in list')

print(find_11([1,2,3,1,2]))

