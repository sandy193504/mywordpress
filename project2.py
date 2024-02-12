#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###Q1. Explain with an example each when to use a for loop and a while loop.

Ans: 
    
For loop:
Use a for loop when you know exactly how many times you need to iterate. This means you have a definite starting and ending point for your loop. 
example:
You want to print the squares of the first 5 numbers.

while loop:
Use a while loop when you don't know beforehand how many times you need to iterate. The loop will continue as long as a certain condition is met. 
example:
You want to keep reading user input until they type "quit".

###Q2. Write a python program to print the sum and product of the first 10 natural numbers using for and while loop.

# Calculate sum
sum_of_numbers = 0
for i in range(1, 11):
  sum_of_numbers += i

# Calculate product
product_of_numbers = 1
for i in range(1, 11):
  product_of_numbers *= i

# Print results
print("The sum of the first 10 natural numbers is:", sum_of_numbers)
print("The product of the first 10 natural numbers is:", product_of_numbers)

##END

# Calculate sum
i = 1
sum_of_numbers = 0
while i <= 10:
  sum_of_numbers += i
  i += 1

# Calculate product
i = 1
product_of_numbers = 1
while i <= 10:
  product_of_numbers *= i
  i += 1

# Print results
print("The sum of the first 10 natural numbers is:", sum_of_numbers)
print("The product of the first 10 natural numbers is:", product_of_numbers)


### Q3. Create a python program to compute the electricity bill for a household.
"""The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
You are required to take the units of electricity consumed in a month from the user as input.
Your program must pass this test case: when the unit of electricity consumed by the user in a month is
310, the total electricity bill should be 2250."""


units_consumed = int(input("Enter the number of units consumed: "))

if units_consumed <= 100:
  bill = units_consumed * 4.5
elif units_consumed <= 200:
  bill = 100 * 4.5 + (units_consumed - 100) * 6
elif units_consumed <= 300:
  bill = 100 * 4.5 + 100 * 6 + (units_consumed - 200) * 10
else:
  bill = 100 * 4.5 + 100 * 6 + 100 * 10 + (units_consumed - 300) * 20

print("Total electricity bill:", bill)


""" Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
that list."""

# Using a for loop

cubes_divisible_by_4_or_5 = []

for num in range(1, 101):
  cube = num**3
  if cube % 4 == 0 or cube % 5 == 0:
    cubes_divisible_by_4_or_5.append(num)

print("Numbers from 1 to 100 whose cubes are divisible by 4 or 5 (using for loop):", cubes_divisible_by_4_or_5)


# Using a while loop

cubes_divisible_by_4_or_5 = []
num = 1

while num <= 100:
  cube = num**3
  if cube % 4 == 0 or cube % 5 == 0:
    cubes_divisible_by_4_or_5.append(num)
  num += 1

print("Numbers from 1 to 100 whose cubes are divisible by 4 or 5 (using while loop):", cubes_divisible_by_4_or_5)

###Write a program to filter count vowels in the below-given string. string = "I want to become a data scientist

string = "I want to become a data scientist"
vowels = "aeiou"

vowel_count = 0
for char in string:
  if char.lower() in vowels:
    vowel_count += 1

print("Number of vowels in the string:", vowel_count)

