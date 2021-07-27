# First Program is used jokingly as this is really an amalgam 

# This is a quick run through on primitives with python
print('Welcome to the Hamster cage. This is what a file looks like when a hamster is learning python')
# print(type(2))
# print(type(True))
# # in earlier versions this number would be a long instead of an int
# print(200000000000);
# test = "words"
# print('test', test);
# # single characters are considered strings
# print('a')

# # vars in Python3
# number = 2
# real = 2.2
# word = "word"
# print(word)
# print(type(word))
# a = b = c = 1.5
# print(a, b, c)
# one, two, three = 1, 'two', 3.0
# print (one, two, three)
# number = 1
# stringz = 'string'
# number = stringz
# # do not have to worry about initializing type
# print(number, str)
# # import magic
# import keyword
# # viewing all keywords on the fly is slightly more convenient than an error or google foo lol
# print(keyword.kwlist)

# indentation or tab seperates blocks of code
# def test():
#       msg = 'fire the cannons'
#       print(msg)
# test()

## allows you to clear a screen when running in a terminal setting... not sure, doubtfult this is necessary
# import os
# clear = lambda: os.system('cls')
# clear()

# shift cmd P to open a repl 
"""
 F5 will open a debug mode for Python
 Also, note the variations in comment styles
 The triple quotes won't display in bytecode
"""

## operators # + - /
## ** exponent 
## any inclusion of a floating point operand will result in a floating point
## older versions of python won't return floating points when dividing
## // floored values output
## % modulo

# operator precedence pemdmas
"""""
()
**
*
/
%
+
-
"""

## bitwise operators 
# << shifts right (leading operator << number of spaces)
# >> shifts left (leading operator << number of spaces)
# ^ xor
# XOR, also known as "exclusive or", compares two binary numbers bitwise.
# If both bits are the same, XOR outputs 0 . 
# If the bits are different, XOR outputs 1
# &  It returns TRUE if both the operands (right side and left side) are true
# | It returns TRUE if either of the operand (right side or left side) is true


#string manipulation 
# string = 'I am a Python based hamster'
# stringI = 'I am a Python based hamster'
# string[0]
# print(string[0])
# print(string[-1])
# # len is the .length of Bredan Eich's world 
# print(len(string))
# # way slicker than substrings, slices, splices, etc. imo
# print(string[5:11])
# print(string[:27])
# # concatenation is the same, but type conversion isn't the same
# print(2 * string)
# word = "Ford"
# word = "L" + word[1:]
# print(word)
# print('word', word);

# format method
# print("Today I had {0} cups of coffee {1}".format(3, "coffee"))
# print('prices: ({x}, {y}, {z})'.format(x = 2.0, y = 1.5, z = 5))
# print('The {vechicle} had {0} crashes in {1} months'.format(5, 6, vechicle = 'truck'))
# # left right align 
# print('{:<20}'.format("text"))
# print('{:>20}'.format("text"))
# # binary
# print('{:b}'.format(21))
# # hexadecimal
# print('{:x}'.format(21))
# # octal
# print('{:o}'.format(21))

# print('I am a string "python"')
# print('I\'m atring in "python"')
# # r 
# print(r'c:\number\nan')
# # triple quotes allow for literals
# print("""
#       I'm a 
# young lad
#       in the world of
#       'Python'
# """)

# conditional operators: < > <= >= != == 
# false 0 true 1
# print(5 < 6)
# print(2 == 2)
# print(2 >=3)
# print(4 != 1)
# print(0 == False)
# print(2 == True)
# print('abc' == 'cba')

"""
priority arrangement: 
 not 
 and 
 or
"""
# a = True
# b = False
# both conditions must be true return true
# print(a and b)
# print(b and b)
# print(a and a)
# true for either condition results in true
# print(a or a)
# print(b or b)
# print(a or b)

# d = 5
# e = 1
# f = False
# g = 'python'
# h = 'some'
# z = not((not(e <= d) and (g >= h)) or f) and 1
# print(z)

# passerby_speech = "Hi"

# if passerby_speech == 'hello':
      # print("Hi")
# elif passerby_speech == 'Hi':
#       print("Hello")
# else :
#       print('Hey, whatcha doing hamster lad')

# if 5 >  7:
#       if 5 > 6:
#              print('5 > 6')
#       else:
#              print('5 <= 6')
# else: 
#       print(" not true!")

# num = 3

# if( num > 1 and num < 5):
#       print(num)
# elif(num > 2 and num < 4):
#       print(num+1)
# else:
#       print(num-1)

#ternary is conducted inline via conditionals
# passerby_speechI = "Hello"
# me = "Hi" if passerby_speechI == "Hello" or passerby_speechI == "Hi" else "Hey"
# print(me)

# a = 3
# a = 7 if 3**2 > 9 else 14
# print(a)

# for loops
# range(start, stop, step)
# for i in range(1,10,3):
#       print(i)

# string = "String traversal"
# for i in range(len(string)):
#       print(string[i])

# for char in string:
#       print(char)

# for i in range(3):
#       for j in range(2):
#             print(j)

# looping a table
# for i in range(1, 11):
#       print('{:<3}|'.format(i), end="")

#       for j in range(1,11):
#             print('{:>4}'.format(i * j),end="")
#       if i == 1:
#             print('\n{:#^44}'.format(""),end="")

#       print("")

#while
# condition = 10
# while condition != 0:
#       print(condition)
#       condition = condition - 1

# while True: 
#       print("Infinite")
#       break

# skip steps in a command via "continue"
# for i in range(1, 11):
#       if i == 5:
#             continue
#       print(i)

#Functions
# def function():
#       print("This is our first function!")

# function()

# def returning():
#       return "I am result"

# result = returning()
# print(result)

# def multival():
#       return "this is a result,",2
# print(multival()[1]) 

# functions with arguments 
# def parameters(a):
#       print(a)

# parameters("This is a parameter")

# def add(a,b):
#       c = a + b
#       return c

# result = add(12,5)
# stringResults = add("twelve", "five")
# print(stringResults)

# defaults can be overridden, functions pass by value not reference
# def default_param(a, b = 4,c = 5):
#       return a + b + c
# result = default_param(3, 7, 9)
# print(result)

#local scope good aritcle that articulates scope better than this 
#tutorial https://www.educba.com/scope-in-python/
# def scope(a):
#       a = a + 1
#       print(a)
#       return a
# scope(5)

# nested functions 
# def outer(a):

#       def nested(b):
#             return b * a
            
#       a = nested(a)
#       return a

# print(outer(4))

#passing args to nested functions... spicy
# def f(a):
#       def g(b):
#             def h(c):
#                   return a * b * c
#             return h
#       return g
# print(f(5)(2)(3))

# recursive functions (functions that calls itself)
# factorial the product of an integer and all the integers below it
# def factorial(n):
#       if n == 1:
#             return 1
#       else:
#             return n * factorial(n - 1)
# print(factorial(5))

# # regular recursion
# def sum(n):
#       if n == 1:
#             return 1
#       else: 
#             return n + sum(n-1)

# #tailed recursion            
# def tail_sum(n, accumlator = 0):
#       if n == 0:
#             return accumlator
#       else: 
#             return tail_sum(n-1, accumlator + n)

# print(sum(10))
# print(tail_sum(10))

# #Lambda functions no name when defining it, and it is contained in one line of code. 
# # JS comparision === ES6 arrow functions or functions expressions resulting in anonymous functions
# f = lambda x, y: x + y

# print(f(2,3))

# g = lambda a: lambda b: lambda c: a * b * c

# print(g(1)(2)(3))

# h = lambda c: lambda a,b: lambda d: (c * (a + b)) % d

# print(h(2)(4,3)(11))

# exception handling

# print(5/0)``

# file = open("file", "r")

# int('1.2')

# try:
#       a = 5/0
#version 2 syntax
# except Exception, e:
# except Exception as e:
#       print(e)

# try:
#       n = int(input("Enter an Integer: "))
# except ValueError:
#       print("That is not an integer")

# try: 
#       sum = 0
#       file = open('numbers.txt', 'r')
#       for number in file:
#             sum = sum + 1.0/int(number)
#       print(sum)
# except ZeroDivisionError:
#       print("Number in file eqaul to zero")
# except IOError:
#       print("File does not exist")
# finally: 
#       print(sum)
#       file.close

#exception handling

# a = 1 

# def RaiseException(a):
#       if type(a) != type('a'):
#             raise ValueError("This is not a string")
# try: 
#       RaiseException(a)
# except ValueError as e:
#       print(e)

# def TestCase(a, b):
#       assert a < b, "a is greater than b"
# try:
#       TestCase(2,1)
#       print(a, b)
# except AssertionError as e:
#       print(e)

#Data Inupt
#raw_input was used in V2
# age = input("How old are you: ")
# print(age)

#File Mangement
#open(filename, read/write, buffering)

# file = open("/Users/nathanbauer/repos/python101/text.txt","r")
# print(file.read())
# print(file.read(11))
# # print(file.tell())
# file.seek(12)
# print(file.tell())
# for line in file:
#       print(line)
# file.close()
# print("File Name:  " + file.name)
# print(str(file.closed))
# print("Mode " + file.mode)

#File management
#w+ allows generic writing
#wb allows bitewise operations
file = open("/Users/nathanbauer/repos/python101/textII.txt", "w+")
file.write("Deploy the hamster army")
file.seek(0)
file.write("Re-deploy ")
print(file.read())
file.close()

#Data Structures


