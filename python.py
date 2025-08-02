### MY PYTHON CODE

#### *1. Hello, World!*
#Write a Python program to print "Hello, World!" to the console.

print("Hello, World!")

### *2. Sum of Two Numbers*
#Write a program that takes two numbers as input and prints their sum.

def main():
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        total = number1 + number2
        
        print("The sum of", number1, "and", number2, "is:", total)
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
main()

#### *3. Check Even or Odd*
#Write a program to check if a given number is even or odd.
def check_even_odd():
    try:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

check_even_odd()


#### *4. Largest of Three Numbers*
#Write a program to find the largest of three numbers entered by the user


def find_largest():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        if num1 >= num2 and num1 >= num3:
            largest = num1
        elif num2 >= num1 and num2 >= num3:
            largest = num2
        else:
            largest = num3
        
        print("The largest number is:", largest)
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
find_largest()

#### *5. Factorial of a Number*
#Write a program to calculate the factorial of a given number using a loop.

def factorial():
    try:
        num = int(input("Enter a non-negative integer: "))
        
        if num < 0:
            print("Factorial is not defined for negative numbers.")
            return

        result = 1
        for i in range(1, num + 1):
            result *= i

        print(f"The factorial of {num} is: {result}")

    except ValueError:
        print("Invalid input. Please enter a whole number.")

factorial()

#### *6. Print Multiplication Table*
#Write a program to print the multiplication table of a given number.

def multiplication_table():
    try:
        num = int(input("Enter a number: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Please enter a valid integer.")

multiplication_table()

#### *7. Check Prime Number*
#Write a program to check if a given number is a prime number.

def is_prime():
    try:
        num = int(input("Enter a number: "))
        if num < 2:
            print(f"{num} is not a prime number.")
            return
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                return
        print(f"{num} is a prime number.")
    except ValueError:
        print("Please enter a valid integer.")

is_prime()

#### *8. Fibonacci Sequence*
#Write a program to generate the first n terms of the Fibonacci sequence.

def fibonacci_sequence():
    try:
        n = int(input("Enter the number of terms: "))
        a, b = 0, 1
        for _ in range(n):
            print(a, end=' ')
            a, b = b, a + b
        print()
    except ValueError:
        print("Please enter a valid integer.")

fibonacci_sequence()

#### *9. Reverse a String*
#Write a program to reverse a given string.

def reverse_string():
    text = input("Enter a string: ")
    reversed_text = text[::-1]
    print("Reversed string:", reversed_text)

reverse_string()

#### *10. Count Vowels in a String*
#Write a program to count the number of vowels in a given string.

def count_vowels():
    text = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    print("Number of vowels:", count)

count_vowels()

#### *11. Palindrome Check*
#Write a program to check if a given string is a palindrome.

def is_palindrome(text):
    if text == text[::-1]:
        print("It's a palindrome.")
    else:
        print("Not a palindrome.")

is_palindrome(input("Enter a string: "))

#### *12. Find the Maximum in a List*
#Write a program to find the maximum number in a list of numbers.

numbers = [5, 12, 7, 22, 3]
maximum = max(numbers)
print("Maximum number:", maximum)

#### *13. Find the Minimum in a List*
#Write a program to find the minimum number in a list of numbers.

numbers = [5, 12, 7, 22, 3]
minimum = min(numbers)
print("Minimum number:", minimum)

#### *14. Sum of List Elements*
#Write a program to calculate the sum of all elements in a list.

numbers = [5, 12, 7, 22, 3]
total = sum(numbers)
print("Sum of elements:", total)

#### *15. Remove Duplicates from a List*
#Write a program to remove duplicates from a list.

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)

#### *16. Check if a Number is in a List*
#Write a program to check if a given number exists in a list.

numbers = [5, 12, 7, 22, 3]
target = int(input("Enter number to search: "))
print("Found!" if target in numbers else "Not found.")

#### *17. Count Words in a String*
#Write a program to count the number of words in a given string.

text = input("Enter a sentence: ")
words = text.split()
print("Word count:", len(words))

#### *18. Find the Length of a String*
#Write a program to find the length of a string without using the len() function.

text = input("Enter a string: ")
count = 0
for _ in text:
    count += 1
print("Length of string:", count)

#### *19. Swap Two Variables*
#Write a program to swap the values of two variables without using a temporary variable.

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
a, b = b, a
print("After swap: a =", a, ", b =", b)

#### *20. Generate a Random Number*
#Write a program to generate a random number between 1 and 100.

import random
print("Random number between 1 and 100:", random.randint(1, 100))

