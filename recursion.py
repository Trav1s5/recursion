"""1]Define a recursive function that takes two integers as input and returns their product using
repeated addition, without employing the multiplication operator. """
def productUsingRepeatedAddition(a,b):
    if b==0:
        return 0
    elif b>0:
        return a+ productUsingRepeatedAddition(a,b -1)
    else:
         return -productUsingRepeatedAddition(a,-b)#if b is negative it converts it to positive and flips the sign of the result
print(productUsingRepeatedAddition(2,9))

"""2]Define a recursive function that computes the result of raising a given base to a specified 
exponent, without using the exponentiation operator(**) """

def raisingBaseWithoutExp(b,exp):
    #base case
    if exp==0:
        return 1
    #handle negative exp
    elif exp<0:
        return 1 / raisingBaseWithoutExp(b,-exp)
    else:
        return b *raisingBaseWithoutExp(b,exp-1)
print(raisingBaseWithoutExp(1,23))


"""3]Implement a recursive function that prints all integers from a given number n down to 0"""

def countdown(n):
    #base case
    if n<0:
        print(" ")
    #recursive case
    else:
        print(n)
        countdown(n-1)

countdown(10)

"""4]Implement a recursive function that prints all integers from 0 up to a given number n by modifying 
the previous countdown function. """

def countup(n):
    #base case stops when we reach 0
    if n<0:
       return None
    #recursive case
    else:
        countup(n-1)
        print(n)

countup(5)

"""5]Write a recursive function that takes a string as input and returns a reversed copy of the string, 
using only string concatenation."""



"""Solution Six"""


"""Solution Seven"""

