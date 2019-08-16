# ''' fibonacci series'''

# def fib(n):
# 	if n < 2:
# 		return n
# 	else:
# 		nums[0,1]
# 		new_num = nums[-1] +nums[-2]
# 		nums.append(new_num)
# 	return nums[-1]

# 	def fibonacci(n):
#     """ compute the nth Fibonacci number """

#     if n < 2:
#         return n

#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a

# def fibonacci(n):
# 		if n < 2:
# 				return n
# 		else:
# 				return fibonacci(n-1) +fibonacci(n-2)

# assert fibonacci(5) == 5

# def pig_latin(word):
# 		first_letter = word[0]
# 		# check if vowel
# 		if first_letter in 'aeiou':
# 				pig_word = word + 'ay'
# 		else:
# 			pig_word = word[1:] + first_letter + 'ay'

# 		return pig_word

# print(pig_latin('word'))

def even_num(*args):
	even_num = []
	for num in args:
		if num % 2 != 0:
			pass
		else:
			even_num.append(num)
	return even_num

print(even_num(2,3,4,5,6))


def skyline(mystring):
	newstring = ''

	for i in range(len(mystring)):
		if i%2 ==0:
			newstring += mystring[i].upper()
		else:
			newstring += mystring[i].lower()
	return newstring

print(skyline('AHgbjekjhd'))
