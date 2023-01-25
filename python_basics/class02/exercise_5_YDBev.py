'''
Edit this file to complete Exercise 5
'''

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# divisible: (of a number) capable of being divided by another number without a remainder.
# multiple: a number that can be divided by another number without a remainder.
def find_num_div7andmult5():
    '''
    This program is to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
    Leave() empty!
    Execute 'ind_num_div7andmult5()' to see the results
    '''
    a=list(range(1500, 2701)) # list of numbers from 1500 to 2700
    num = [] # initialize an empty list to put in numbers that fit the condition
    for i in range(0,(len(a))) : # x = list(range(1500, 2701)
        if a[i]%7==0 and a[i]%5==0 :
            num.append(a[i])

    print(f'Last index counter i: {i} \nFirst number checked: {a[0]} \nLast number checked: {a[i]}')
    print(f'{len(num)} Numbers fit the condition: \n{num}')




# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

def num_odd_even(x):
    '''
    This program is to find number of odd and even numbers from a series of numbers
    x: input series of numbers/integers
    '''
    num_even = []
    num_odd = []
    for i in range(0,(len(x))) :
        if x[i]%2==0:
            num_even.append(x[i])
        else :
            num_odd.append(x[i])
        len(num_even)
        len(num_odd)
    # print(f'Even list: {num_even}')
    # print(f'Odd list: {num_odd}')
    # print(f'i: {i}. len(x): {len(x)}')
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
def fizzbuzz():
    '''
    This program is print 'Fizz' for mutiples of three, print 'Buzz' for mutiples of five, and 'FizzBuzz' for both multiples of three and five
    Leave() empty!
    Execute 'fizzbuzz()' to see the results
    '''
    a=list(range(0, 51))
    fizzbuzz=[]
    for i in range(0,(len(a))):
        if a[i]%3==0 and not a[i]%5==0:
            print('Fizz')
        elif a[i]%5==0 and not a[i]%3==0:
            print('Buzz')
        elif a[i]%3==0 and a[i]%5==0:
            print('FizzBuzz')
        else :
            print(a[i])
    print(fizzbuzz)




# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

def num_div5_150max(x):
    '''
    This program is to find number numbers which are divisible by 5 and stop the loop once number is greater than 150
    x: input series of numbers/integers
    '''
    for i in range(0,(len(x))) :
        if x[i]%5==0 and x[i]<=150 :
            print(x[i])
        elif x[i]>150:
            break




# 5. Pick one of the questions above and use range() for a different solution

# Use question 1
def find_num_div7andmult5_altrange():
    '''
    This program is to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
    Leave() empty!
    Execute 'ind_num_div7andmult5()' to see the results
    '''
    a=list(range(1500, 2701)) # list of numbers from 1500 to 2700
    num = [] # initialize an empty list to put in numbers that fit the condition
    for i in range(0,(len(a)-1)) : # x = list(range(1500, 2701) or range(len(a))
        if a[i]%7==0 and a[i]%5==0 :
            num.append(a[i])
            i+=1
    print(f'Last index counter i: {i} \nFirst number checked: {a[0]} \nLast number checked: {a[i]}')
    print(f'{len(num)} Numbers fit the condition: \n{num}')




# 6. Pick one of the question above and use comprehension for a different solution

# Use question 3
a=list(range(0, 51))
fizzbuzz_comp = [print('Fizz') if a[i]%3==0 and not a[i]%5==0 else print('Buzz') if a[i]%5==0 and not a[i]%3==0 else print('FizzBuzz') if a[i]%3==0 and a[i]%5==0 else print(a[i]) for i in range(0,(len(a)))]




# 7. Pcik one of the questions above and use while loop for a different solution

# Use question 4
def num_div5_150max_while(x):
    '''
    This program is to use while loop to find number numbers which are divisible by 5 and stop the loop once number is greater than 150
    x: input series of numbers/integers
    '''
    i=0
    while x[i] <=150:
        if x[i]%5==0:
            print(x[i])
        i+=1


# might be helpful to add here if run .py file in command line
if __name__ == '__main__': 
    pass
