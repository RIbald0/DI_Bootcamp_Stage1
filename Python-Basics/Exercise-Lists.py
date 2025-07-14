#Exercise 1 : Lists
#1.Given a list [1, 2, 3, 4], print out all the values in the list one by one.
list = [1, 2, 3, 4]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
#2.Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.
list = [1, 2, 3, 4]
print(list[0]*20)
print(list[1]*20)
print(list[2]*20)
print(list[3]*20)
#3.Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].
names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters)
#4.Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6].
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
#5.Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists: [3, 4].
numbers_first = [1, 2, 3, 4]
numbers_second = [3, 4, 5, 6]
common_numbers = [num for num in numbers_first if num in numbers_second]
print (common_numbers)
#6.Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: ["eile", "mit", "ttam"].
names = ["Elie", "Tim", "Matt"]
reversed_names = [name[::-1].lower() for name in names]
print(reversed_names)
#7.Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].  
first = "first"
second = "third"
common_letters = [letter for letter in first if letter in second]
print(common_letters)
#8.For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].
for number in range(1, 101):
 if number % 12 == 0:
   print(number)
#9.Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].
word = 'amazing'   
vowels = 'aeiou'
no_vowels = [letter for letter in word if letter not in vowels]  
print(no_vowels)
#10.Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]. 
result = [[i for i in range(3)] for _ in range(3)]
print(result)
#11.Generate a list with the following structure:
grid = [[i for i in range(10)] for _ in range(10)]
print(grid)