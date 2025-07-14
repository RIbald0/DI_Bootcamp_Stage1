#Exercise 1 : Add Two Numbers
#Write a function add_two_numbers that takes two numbers as parameters and returns their sum.
def add_two_numbers(a,b):
    return a + b
print(add_two_numbers(3,5))
print(add_two_numbers(10,20))
#Exercise 2 : Print a Greeting
#Write a function greet that takes one parameter, a person’s name, and prints a greeting message like “Hello, [name]!”.
def greet(name):
  return(f"Hello, {name}!")
print(greet("Alice"))
#Exercise 3 : Check if Number is Even or Odd
#Write a function check_even_odd that takes one number and prints “Even” if the number is even, and “Odd” if the number is odd.
def even_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"
print(even_odd(5))
print(even_odd(4))
#Exercise 4 : Sum of Numbers in a List
#Write a function sum_list that takes a list of numbers as a parameter and returns the sum of all numbers in the list.
def sum_list(numbers):
  total = 0
  for number in numbers:
    total += number
  return total
numbers = [1, 2, 3, 4]
print(sum_list(numbers))

#Exercise 5 : Print Days of the Week
#Write a function print_days that prints the days of the week (Sunday, Monday, Tuesday, etc.) using a loop.
def print_days():
    days_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in days_week:
        print(day)
print_days()

# Exercise 6 : Check if Number is Positive, Negative, or Zero
#Write a function check_sign that takes a number and prints whether the number is positive, negative, or zero.
def check_sign(number):
    if number > 0:
         return "Positive"
    elif number == 0:
         return "Zero"
    else:
         return "Negative"
print(check_sign(5))
print(check_sign(-3))
print(check_sign(0))

#Exercise 7 : Repeat a Word
#Write a function repeat_word that takes a word and a number as parameters and prints the word that many times.

def repeat_word(word, number):
    for _ in range(number):
        print(word)
repeat_word("Hello", 3)