# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 22:22:19 2016

@author: naman
"""
number = int(input("What integer do you want the square too of ? "))
guess = 1
iteration = 0
answer = 0

# Used the algorithm that a good guess for square root of a number x when earlier 
# guess was g is g + (x/g)

# Security measure to not calculate square root of a negative number
if number < 0 :
    print("Umm Sorry ! Negative integers don't have any real square roots :(")

# Calculate the square root now !
else :
    while abs((guess * guess) - number) >= 0.0000001 :

# I want to keep a note of how many iterations were done to get the value.
        iteration += 1
        guess = ((guess + (number/guess))/2)
    answer = round(guess, 2)
    print(answer)
    print("Number of times I had to go through code to get the result = " + str(iteration))