# --------------------------------------------------------------------


"""TOPIC: Python Basics Variable"""

# ------------------------------------

""" 1. Declare two variables, `x` and `y`, and assign them integer values. Swap the
values of these variables without using any temporary variable."""

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print("Before swapping: x =", x, "y =", y)
x, y = y, x
print("After swapping: x =", x, "y =", y)

# ------------------------------------

"""2. Create a program that calculates the area of a rectangle. Take the length and
width as inputs from the user and store them in variables. Calculate and
display the area."""

L = int(input("Enter the length of the rectangle: "))
W = int(input("Enter the Width of the rectangle: "))
Area = L * W 
print("The area of the rectangle is", Area)

# ------------------------------------

"""3. Write a Python program that converts temperatures from Celsius to
Fahrenheit. Take the temperature in Celsius as input, store it in a variable,
convert it to Fahrenheit, and display the result."""

C = int(input("Enter the temperature in Celsius: "))
F = (C * 9/5) + 32
print("The temperature in Fahrenheit is", F)



# --------------------------------------------------------------------

"""TOPIC: String Based Questions"""


"""1. Write a Python program that takes a string as input and prints the length of
the string."""

string = input("Enter the String: ")
print("The Lenght of the String is: ", len(string))

# ------------------------------------

"""2. Create a program that takes a sentence from the user and counts the number
of vowels (a, e, i, o, u) in the string."""

sentence = input("Enter the sentence: ")
count = 0
for i in sentence:
    if i in "aeiouAEIOU":
        count += 1
print("The number of vowels in the sentence is: ", count)

# ------------------------------------

"""3. Given a string, reverse the order of characters using string slicing and print
the reversed string.0"""

# version 1 : Using Slicing - This is the best way to reverse a string in Python, by using the reverse indexing technique.

string = input("Enter the String: ")
print("The reversed String is: ", string[::-1])

# version 2 : Using reversed() function - This function returns the reversed iterator of the given string and then its 
# elements are joined empty string separated using join().
string = input("Enter the String: ")
reversed_string = "" . join(reversed(string))
print("The reversed String is: ", reversed_string)

# version 3 : Using for loop - In this method, we will run a loop in reverse order and concatenate characters of string
# in a variable and print the variable.
string = input("Enter the String: ")
reversed_string = ""
for i in string:
    reversed_string = i + reversed_string
print("The reversed String is: ", reversed_string)

# version 4 : Using a Stack - In this method, we will use a stack data structure to reverse the string. We will push
# characters of string in a stack and then pop characters from the stack one by one and concatenate them to a variable
# to get the reversed string.
string = input("Enter the String: ")
reversed_string = ""
stack = []
for i in string:
    stack.append(i)
for i in range(len(stack)):
    reversed_string += stack.pop()
print("The reversed String is: ", reversed_string)


# ------------------------------------

"""4. Write a program that takes a string as input and checks if it is a palindrome
(reads the same forwards and backwards)."""

# Version 1 : Using Slicing

string = input("Enter the String: ")
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# Version 2 : Using for loop
string = input("Enter the String: ")
reversed_string = ""
for i in string:
    reversed_string = i + reversed_string
if string == reversed_string:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# Version 3 : Using a Reversed() function
string = input("Enter the String: ")
if reversed_string == reversed(string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


# ------------------------------------

"""5. Create a program that takes a string as input and removes all the spaces from
it. Print the modified string without spaces."""

# Version 1 : Using replace() function
string = input("Enter the String: ")
string = string.replace(" ", "")
print("The modified string is: ", string)


# Version 2 : Using join() and split() function
string = input("Enter the String: ")
string = "".join(string.split())
print("The modified string is: ", string)


# Version 3 : Using for loop
string = input("Enter the String: ")
modified_string = ""
for i in string:
    if i != " ":
        modified_string += i
print("The modified string is: ", modified_string)




