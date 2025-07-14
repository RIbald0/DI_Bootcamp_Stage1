#1.Declare a variable called first and assign it to the value "Hello World"
first = "Hello World" 
#2.Write a comment that says "This is a comment."
#This is a comment
#3.Log a message to the terminal that says "I AM A COMPUTER!"
print ("I AM A COMPUTER!")
#4.Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."
if 1<2 and 4>2:
 print ("Math is fun!")
#5.Assign a variable called nope to an absence of value.
nope = None
#6.Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value.
result = True and False
#7.Calculate the length of the string "What's my length?"
text = "What's my length?"
lenght = len(text)
print(lenght)
#8.Convert the string "i am shouting" to uppercase
text = "i am shouting"
uppercase_text = text.upper()
print (uppercase_text)
#9.Convert the string "1000"to the number 1000
num = int("1000")
print (num)
#10.Combine the number 4 with the string "real" to produce "4real"
num = 4
text = "real"
print(f"{num}{text}")
#11.Record the output of the expression 3 * "cool"
print (3 * "cool")
#12.Record the output of the expression 1 / 0
#print (1 / 0) It gives ZeroDivisionError: division by zero
#13.Determine the type of []
print(type([]))
#14.Ask the user for their name, and store it in a variable called name
name = input("Enter your name: ")
print(name)
#15.Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!" If the number is positive, show a message that says "That number is greater than 0!" Otherwise, show a message that says "You picked 0!
number = int(input("Enter a number: "))
if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else: 
   print("You picked 0!")
#16.Find the index of "l" in "apple"
word = "apple"
index = (word.index("l"))
print(index)
#17.Check whether "y" is in "xylophone"
word = "xylophone"
if "y" in word:
  print("y is in xylophone")
#18.Check whether a string called my_string is all in lowercase
string = "my_string"
if string.islower():
 print ("my_string is all in lowercase")

#Exercise 2 Cat's and dog's years
def pet_years (human_years):
  if human_years == 1:
    cat_years = 15
    dog_years = 15
  elif human_years == 2:
    cat_years = 15+9
    dog_years = 15+9
  else:
    cat_years = 15 + 9 + (human_years - 2) * 4
    dog_years = 15 + 9 + (human_years - 2) * 5
  return [human_years, cat_years, dog_years]
print(pet_years(10))
print(pet_years(1))
print(pet_years(2))