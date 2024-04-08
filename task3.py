#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a=5, b=1, c=11
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

question = "What is the value of a?"
a = input(question)
a = int(a)

question = "What is the value of b?"
b = input(question)
b = int(b)

question = "What is the value of c?"
c = input(question)
c = int(c)

x = (c-b)/a

print(f"The answer for x is {x}")
