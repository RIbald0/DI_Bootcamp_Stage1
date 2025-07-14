#1.Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).
list = [("name", "Elie"), ("job", "Instructor")]
dictionary = dict(list)
print(dictionary)
#2.Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
first_list = ["CA", "NJ", "RI"]
second_list = ["California", "New Jersey", "Rhode Island"]
dictionary = dict(zip(first_list, second_list))
print(dictionary)
#3.Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
vowels = "aeiou"
vowel_dict = {char: 0 for char in vowels}
print(vowel_dict)
#4.Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself. You should return something like this: {1: "a", 2: "b", 3: "c", ...}
alphabet = "abcdefghijklmnopqrstuvwxyz"
number_dict = {i+1: char for i, char in enumerate(alphabet)}
print(number_dict)
#Bonus.Given the string "awesome sauce", return a dictionary where the keys are vowels, and the values are the count of each vowel in the string. Your dictionary should look like this: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}.
word = "awesome sauce"
vowels = "aeiou"
vowel_count = {vowel: word.count(vowel) for vowel in vowels}
print(vowel_count)