'''
Exercise 5
'''

# 1. rite a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here
mul_35 = []
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        mul_35.append(i)
print(mul_35)

# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
num_even = []
num_odd = []
for i in numbers:
    if i%2==0:
        num_even.append(i)
    else:
        num_odd.append(i)
print(f'Number of even numbers : {len(num_even)}')
print(f'Number of odd numbers : {len(num_odd)}')

# 3. Write a Python program which iterates the integers from 0 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# Expected Output :
# >>> fizzbuzz
# >>> 1
# >>> 2
# >>> fizz
# >>> 4
# >>> buzz
# >>> ...

# code up your solution here
for i in range(51):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if i<=150 and i%5==0:
        print(i)

# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here
# here's another solution for problem 2
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
num_even = []
num_odd = []
for i in range(len(numbers)):
    v = numbers[i]
    if v%2==0:
        num_even.append(v)
    else:
        num_odd.append(v)
print(f'Number of even numbers : {len(num_even)}')
print(f'Number of odd numbers : {len(num_odd)}')

# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here
# here's comprehensive solution for problem 4
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
com = [i for i in list1 if i<=150 and i%5==0]
print(com)

# 7. Pcik one of the questions above and use while loop for a different solution

# code up your solution here
# here's the while loop solution for problem 1
mul_35 = []
i = 1500
while i<=2700:
    if i%7==0 and i%5==0:
        mul_35.append(i)
    i += 1
print(mul_35)


'''
Exercise 6
'''

def calculation(a, b):
	'''
	Write a function calculation() such that it can accept two variables 
	and calculate the addition and subtraction of it. 
	It must return both addition and subtraction in a single return call

	Expected output:
	res = calculation(40, 10)
	print(res)
	>>> (50, 30)

	Arguments:
	a: first number 
	b: second number

	Returns:
	sum: sum of two numbers
	diff: difference of two numbers
	'''

	# code up your solution here
    return a+b,a-b

def triangle_lambda():
	'''
	Return a lambda object that takes in a base and height of triangle
	and computes the area.

	Arguments:
	None

	Returns:
	lambda_triangle_area: the lambda
	'''
    # code up your solution here
    b = float(input('Input the base:'))
    h = float(input('Input the height:'))
    area = lambda b,h: b*h/2
    return area(b=b,h=h)

def sort_words(hyphen_str):
	'''
	Write a Python program that accepts a hyphen-separated sequence of words 
	as input, and prints the words in a hyphen-separated sequence after 
	sorting them alphabetically.

	Expected output:
	sort_words('green-red-yellow-black-white')
	>>> 'black-green-red-white-yellow'
	
	Arguments:
	hyphen_str: input string separated by hyphen

	Returns:
	sorted_str: string in a hyphen-separated sequence after 
	sorting them alphabetically
	'''

	# code up your solution here
    word_list = 'green-red-yellow-black-white'.split('-')
    word_list.sort()
    return '-'.join(word_list)

def perfect_number():
	'''
	Write a Python function to check whether a number is perfect or not.

	A perfect number is a positive integer that is equal to the sum of 
	its proper positive divisors. Equivalently, a perfect number is a number 
	that is half the sum of all of its positive divisors (including itself).

	Example: 6 is a perfect number as 1+2+3=6. Also by the second definition,
	(1+2+3+6)/2=6. Next perfect number is 28=1+2+4+7+14. Next two perfect
	numbers are 496 and 8128.

	Argument:
	number: number to check

	Returns:
	perfect: boolean, True if number is perfect
	'''

	# code up your answer here
    divisors = [i for i in range(1,num) if num%i==0]
    return sum(divisors)==num

if __name__ == '__main__':
	pass