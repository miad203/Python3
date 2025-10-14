# import math
import itertools


# # Problem: Write a Python program to print the numbers from 1 to 10.
# for i in range(-1, 11):
#     print(i)


# # Problem: Write a Python program to calculate the sum of the first 10 natural numbers.
# totall = 0
# for i in range(1, 11):
#     totall += i

# print(totall)

# # Problem: Write a Python program that takes a user inputted string and prints the string in reverse order.
# user: str = input('Enter your world: ')
# print(user[::-1])

# # Problem: Write a Python program that calculates the area of a rectangle with a given width and height.

# x: int = int(input("Enter height of the ractangle: "))
# y: int = int(input("Enter width of the ractangle: "))

# print(f"The area of the ractangle is: {x*y}")


# # Problem: Write a Python program that calculates the sum of all even numbers from 1 to 50.

# totall: int = 0

# for i in range(1, 51):
#     if i % 2 == 0:
#         totall += i

# print(f'Total: {totall}')

# # Problem: Write a Python program that takes a user inputted string and counts the number of vowels in the string.

# vawels: list = ['a', 'e', 'i', 'o', 'u']
# count: int = 0
# user: str = input("Enter your word: ").lower()
# for each_letter in user:
#     if each_letter in vawels:
#         count += 1

# print(count)

# # Problem: Write a Python program that prints all the prime numbers between 1 and 100.


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# for num in range(1, 101):
#     if is_prime(num):
#         print(num, end=" ")

# # Problem: Write a Python program that takes a list of numbers as input and returns the largest number in the list.


# def LargestNumber(numbers):
#     largest_number = 0
#     for each_number in numbers:
#         if each_number >= largest_number:
#             largest_number = each_number
#     return largest_number


# largest_number = LargestNumber([12, 12, 23, 34, 45, 32, 10])
# print(f'The largest number is: {largest_number}')


# # Problem: Write a Python program that takes a list of strings as input and returns the longest string in the list.

# def LargestString(words):
#     largest_str: str = ''
#     for each_word in words:
#         if len(each_word) > len(largest_str):
#             largest_str = each_word
#     return largest_str


# largest_str = LargestString(['hello', 'there', 'how', 'congratulation', 'you'])
# print(f'The largest string is: {largest_str}')


# # Problem: Write a Python program that reads a file and prints its contents to the console.

# with open('pyread.txt') as thefile:
#     reader = thefile.read()
#     print(reader)

# # Problem: Write a Python program that calculates the sum of the first 100 natural numbers.

# for number in range(1, 101):
#     print(number, end=" ")

# # Problem: Write a Python program that takes a user inputted number and checks if it is odd or even.

# user: int = int(input("Enter your number: "))
# if user % 2 == 0:
#     print(f'{user} is even')
# else:
#     print(f'{user} is odd')

# # Problem: Write a Python program that takes a user inputted string and removes all the vowels from the string.

# vawels = ['a', 'e', 'i', 'o', 'u']
# user: str = input("Enter your word to remove vawels: ")
# new_str = ''
# for each_letter in user:
#     if each_letter not in vawels:
#         new_str += each_letter

# print(new_str)

# # Problem: Write a Python program that calculates the area of a triangle with a given base and height.
# base: int = 10
# height: int = 15

# print(f'The area of a triangle is {0.5*base*height}')


# # Problem: Write a Python program that calculates the sum of all odd numbers from 1 to 50.
# total: int = 0
# for number in range(1, 51):
#     if number % 2 != 0:
#         total += number

# print(f'Total 1 to 50 odd number is: {total}')


# # Problem: Write a Python program that takes a user inputted string and counts the number of consonants in the string.
# vawels: list = ['a', 'e', 'i', 'o', 'u']
# user: str = input("Enter your word to count consonant: ")
# count: int = 0

# for each_letter in user:
#     if each_letter not in vawels:
#         count += 1

# print(f'Total consonant letter is {count}')


# # Problem: Write a Python program that takes a list of numbers as input and returns the smallest number in the list.

# def SmallestNumber(numbers):
#     smallest_number = numbers[0]
#     for number in numbers:
#         if number < smallest_number:
#             smallest_number = number
#     return number


# small_number: int = SmallestNumber([1, 2, 5, 3, -1])
# print(small_number)

# # Problem: Write a Python program that takes a list of strings as input and returns the shortest string in the list.


# def SmallestString(words):
#     smallest_str: str = ''
#     for each_word in words:
#         if len(each_word) < len(largest_str):
#             largest_str = each_word
#     return largest_str

# # Problem: Write a Python program that reads a file and writes its contents to another file.


# with open('pyread.txt') as thefile:
#     print('Reading this file!')
#     reader = thefile.read()
# with open('new.txt', 'w') as thefile:
#     writer = thefile.write(reader)

# # Problem: Write a Python program that calculates the area of a circle with a given radius.

# redius: int = int(input('Enter radius: '))
# calculate = math.pi * math.pow(redius, 2)
# print(f'The area of this circle is: {round(calculate, 2)}')

# # Problem: Write a Python program that takes a user inputted number and checks if it is positive or negative.

# user: int = int(
#     input("Enter your number to check is't positive or negetive: "))
# if user >= 0:
#     print(f'{user} is positive')
# else:
#     print(f'{user} is negetive')

# # Problem: Write a Python program that takes a user inputted string and reverses the order of the words in the string.

# user: str = input("Enter your world to get reverse version: ").split(' ')
# reverse = " ".join(user[::-1])
# print(reverse)

# # Problem: Write a Python program that calculates the sum of all numbers from 1 to 100 that are divisible by 3.
# total: int = 0
# for number in range(1, 101):
#     if number % 3 == 0:
#         total += number

# print(total)

# # Problem: Write a Python program that takes a list of numbers as input and returns the average of the numbers in the list.

# user: str = input(
#     "Enter some number to calculate their average(seperate by space): ")
# num_list = [float(x) for x in user.split(' ')]
# total = sum(num_list)
# print(f"Average: {total/len(num_list)}")

# # Problem: Write a Python program that takes a user inputted string and checks if it is a palindrome.


# def is_palindrome(string):
#     string = string.lower()
#     string = ''.join(filter(str.isalnum, string))
#     return string == string[::-1]


# # Problem: Write a Python program that takes a user inputted string and checks if it is a palindrome.
# user: str = input("Enter your word to check palindrome: ")
# if is_palindrome(user):
#     print('This is a palindrome word')
# else:
#     print('This is not palindrome word')

# # Problem: Write a Python program that takes a list of strings as input and concatenates them into a single string.
# user: str = input(
#     'Enter your word to concatenates(seperate by comma): ').split(',')
# concatenate = ''.join(user)
# print(concatenate)

# # Problem: Write a Python program that takes a user inputted string and converts it to title case (i.e. the first letter of each word is capitalized).

# user: str = input('Enter your word to convert title case: ').title()
# print(user)

# # Problem: Write a Python program that takes a list of numbers as input and returns a new list containing only the even numbers.
# user: str = input("Enter some number with separete by space: ").split(' ')
# num_list = [int(x) for x in user if int(x) % 2 == 0]
# print(num_list)

# # Problem: Write a Python program that calculates the factorial of a given number.


# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)


# user: int = int(input('Enter a number to calculate factorial: '))
# total = factorial(5)
# print(f'{user} factorial is {total}')


# # Problem: Write a Python program that takes a user inputted string and checks if it contains only alphabetical characters.
# def is_alpha(string):
#     for char in string():
#         if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
#             return False
#     return True

# # or use built-in isalpha function


# user: str = input('Enter word to check is it alphabate: ')
# if is_alpha(user):
#     print('pass')
# print('fail')

# # Problem: Write a Python program that takes a list of strings as input and returns a new list containing only the strings that have a length of 4 or more characters.


# def LengthFliter(strings):
#     new_str = []
#     for each in strings:
#         if len(each) > 4:
#             new_str.append(each)
#     return new_str


# user: str = input("Enter word separete by comma: ").split(',')

# new_list = LengthFliter(user)
# print(new_list)

# # Problem: Write a Python program that reads a text file and prints the number of words in the file.


# def word_counter(filename):
#     with open(filename) as thefile:
#         reader = thefile.read()
#     reader.replace('\n', ' ')
#     total_word = reader.count(' ') + 1

#     return total_word


# thefile = word_counter('pyread.txt')
# print(f'Total word in this file is: {thefile}')

# # Problem: Write a Python program that takes a list of numbers as input and returns the sum of the squares of the numbers.


# def sq_sum(numbers):
#     result = [math.pow(x, 2) for x in numbers]
#     additon = sum(result)
#     return additon


# var = sq_sum([1, 2, 4, 6, 8])
# print(f'Sum of the squares of the number is: {var}')

# # Problem: Write a Python program that takes a user inputted number and checks if it is a perfect square.


# def parfect_square(number):
#     if number < 0:
#         return False
#     root = number ** 0.5
#     return root * root == number


# user: int = int(input('Enter a number to check this perfectness: '))

# if parfect_square(user):
#     print('Here it is!')
# else:
#     print('This is not perfect')

# # Problem: Write a Python program that takes a list of strings as input and returns a new list containing only the strings that start with the letter 'a'.


# def FilterA(string):
#     string = string.lower()
#     if string[0] == 'a':
#         return True
#     return False


# user: str = input('Enter some word separete by comma: ').split(',')
# alist = []
# for each in user:
#     if FilterA(each):
#         alist.append(each)

# print(alist)


# # Problem: Write a Python program that takes a user inputted number and checks if it is an Armstrong number.

# def armstrong_number(number):
#     num_str = str(number)
#     length = len(num_str)
#     total = 0

#     for char in num_str:
#         digit = int(char)
#         total += digit ** length
#     return total == number


# user: int = input('Enter a number to check armstrong: ')
# if armstrong_number(user):
#     print(f'{user} is armstrong number')
# else:
#     print(f'{user} is not armstrong number')

# # Problem: Write a Python program that takes a list of numbers as input and returns the product of the numbers.


# def calculate_product(numbers):
#     product = 1
#     for each_number in numbers:
#         product *= each_number
#     return product


# product = calculate_product([1, 2, 4])
# print(product)

# # Problem: Write a Python program that takes a user inputted string and checks if it is a valid email address.


# def valid_email(email):
#     if "@" not in email:
#         return False

#     parts = email.split('@')
#     if len(parts) != 2:
#         return False

#     username, domain = parts
#     if '.' not in domain:
#         return False

#     return True


# user: str = input('Enter a email: ')
# if valid_email(user):
#     print(f'{user} is a valid email')
# else:
#     print(f'{user} is not valid!')

# # Problem: Write a Python program that takes a user inputted number and checks if it is a perfect number.


# def perfect_number(number):
#     if number <= 0:
#         return False

#     divisors = []
#     for i in range(1, number):
#         if number % i == 0:
#             divisors.append(i)

#     return number == sum(divisors)


# user: int = int(input("Enter a number to check perfectness: "))
# if perfect_number(user):
#     print(f'{user} is perfect number')
# else:
#     print(f'{user} is not perfect number')

# # Problem: Write a Python program that takes a list of strings as input and returns a new list containing only the strings that end with the letter 's'.


# def endswith_s(strings):
#     new_list = []
#     string = [each.lower for each in strings]
#     for word in string:
#         if word.endswith('s'):
#             new_list.append(word)
#     return new_list


# s_filter = endswith_s(['hello', 'contains', 'is', 'not'])
# print(s_filter)

# # Problem: Write a Python program that reads a text file and counts the number of occurrences of a specific word.


# def count_word_occurrences(filename, target_word):
#     try:
#         with open(filename) as thefile:
#             reader = thefile.read()
#             content = reader.replace('\n', ' ')
#             total = content.count(target_word)

#             return total
#     except FileNotFoundError:
#         print('File not found!')
#         return -1


# count_word = count_word_occurrences('pyread.txt', 'eye')
# print('Target word:', count_word)

# # Problem: Write a Python program that takes a string input and returns the word that occurs the most frequently.


# def most_common_word(string):
#     string = string.lower()
#     all_word = dict()
#     for word in string.split(" "):
#         if word in all_word:
#             all_word[word] += 1
#         else:
#             all_word[word] = 1

#     return max(all_word, key=all_word.get)


# most_common = most_common_word('hello hello hello world')
# print(f'Most common word is: {most_common}')

# # Problem: Write a Python program that takes a list of numbers as input and returns the number that occurs the most frequently.


# def most_common_number(numbers):
#     all_number = dict()
#     for number in numbers:
#         if number in all_number:
#             all_number[number] += 1
#         else:
#             all_number[number] = 1

#     return max(all_number, key=all_word.get)


# most_common = most_common_number([1, 2, 3, 4, 5, 2, 3, 4, 2, 3])
# print(f'Most common number is: {most_common}')

# # Problem: Write a Python program that takes a user inputted string and checks if it is an anagram of another string.


# def is_anagram(string1, string2):
#     string1 = string1.replace(" ", "").lower()
#     string2 = string2.replace(" ", "").lower()

#     return string1 == string2


# usr: str = input("Enter first word: ")
# user2: str = input("Enter second word: ")

# if is_anagram(usr, user2):
#     print('they are anagram')
# else:
#     print('they are not anagram!')

# # Problem: Write a Python program that takes a list of dictionaries as input and sorts the list by a specific key.


# def sort_list_of_dicts(list_of_dicts, sort_key):
#     return sorted(list_of_dicts, key=lambda x: x[sort_key])


# # Example list of dictionaries
# data = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 35}
# ]

# sort_key = input("Enter the key to sort by: ")

# sorted_data = sort_list_of_dicts(data, sort_key)
# print("Sorted List:")
# for item in sorted_data:
#     print(item)

# Problem: Write a Python program that takes a user inputted string and returns all possible permutations of the string.


def permotation(string):
    return itertools.permutations(string)


usr: str = input('Enter word to permotation: ')
permo = permotation(usr)
for x in permo:
    print(''.join(x))
