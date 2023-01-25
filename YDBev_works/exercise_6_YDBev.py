'''
Edit this file to complete Exercise 6
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

	addition = a+b
	substraction = a-b
	print(f'sum of two numbers: {addition}')
	print(f'diff of two numbers: {substraction}')




####### NOT SURE ABOUT the ask for this question, define within enclosed space  ######## 14JAN23
def triangle_lambda():
	'''
	Return a lambda object that takes in a base and height of triangle
	and computes the area.

	Arguments:
	None

	Returns:
	lambda_triangle_area: the lambda
	'''

	print('lambda_triangle_area: the lambda')

## use lambda function to calculate area 
def triangle_lambda(base,height):
    return (lambda base, height : 0.5*base*height)(base,height)




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

    hyphen_sep = hyphen_str.split('-')
    hyphen_sep.sort()
    print('-'.join(hyphen_sep))




def perfect_number(num):
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

    divisor = []
    for i in range(1,x+1):
        if x%i==0:
            divisor.append(i)
    print(f'All divisors of {x}: {divisor}') 

    # # def1: A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
    # x_perfect = x == sum(divisor[0:-1])

    # def2: A perfect number is a number  that is half the sum of all of its positive divisors (including itself)
    num_to_check = sum(divisor)/2
    x_perfect = x == num_to_check
    
    print(f'Is {x} perfect?: {x_perfect}')




if __name__ == '__main__':
	pass