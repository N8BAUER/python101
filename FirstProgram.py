# First Program is used jokingly 

# This is a quick run through on primitives with python
print('welcome')
print(type(2))
print(type(True))
# in earlier versions this number would be a long instead of an int
print(200000000000);
test = "words"
print('test', test);
# single characters are considered strings
print('a')

# vars in Python3
number = 2
real = 2.2
word = "word"
print(word)
print(type(word))
a = b = c = 1.5
print(a, b, c)
one, two, three = 1, 'two', 3.0
print (one, two, three)
number = 1
str = 'string'
number = str
# do not have to worry about initializing type
print(number, str)
# import magic
import keyword
# viewing all keywords on the fly is slightly more convenient than an error or google foo lol
print(keyword.kwlist)

# indentation or tab seperates blocks of code
def test():
      msg = 'fire the cannons'
      print(msg)
test()

## allows you to clear a screen when running in a terminal setting... not sure, doubtfult this is necessary
import os
clear = lambda: os.system('cls')
clear()

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
print("Today I had {0} cups of coffee {1}".format(3, "coffee"))
print('prices: ({x}, {y}, {z})'.format(x = 2.0, y = 1.5, z = 5))
print('The {vechicle} had {0} crashes in {1} months'.format(5, 6, vechicle = 'truck'))
# left right align 
print('{:<20}'.format("text"))
print('{:>20}'.format("text"))
# binary
print('{:b}'.format(21))
# hexadecimal
print('{:x}'.format(21))
# octal
print('{:o}'.format(21))

print('I am a string "python"')
print('I\'m atring in "python"')
# r 
print(r'c:\number\nan')
# triple quotes allow for literals
print("""
      I'm a 
young lad
      in the world of
      'Python'
""")

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
a = True
b = False
# both conditions must be true return true
print(a and b)
print(b and b)
print(a and a)
# true for either condition results in true
print(a or a)
print(b or b)
print(a or b)

d = 5
e = 1
f = False
g = 'python'
h = 'some'
z = not((not(e <= d) and (g >= h)) or f) and 1
print(z)

passerby_speech = "Hi"

if passerby_speech == 'hello':
      print("Hi")
elif passerby_speech == 'Hi':
      print("Hello")
else :
      print('Hey, whatcha doing hamster lad')

if 5 >  7:
      if 5 > 6:
             print('5 > 6')
      else:
             print('5 <= 6')
else: 
      print(" not true!")

num = 3

if( num > 1 and num < 5):
      print(num)
elif(num > 2 and num < 4):
      print(num+1)
else:
      print(num-1)

#ternary is conducted inline via conditionals
passerby_speechI = "Hello"
me = "Hi" if passerby_speechI == "Hello" or passerby_speechI == "Hi" else "Hey"
print(me)

a = 3
a = 7 if 3**2 > 9 else 14
print(a)

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
for i in range(1, 11):
      print('{:<3}|'.format(i), end="")

      for j in range(1,11):
            print('{:>4}'.format(i * j),end="")
      if i == 1:
            print('\n{:#^44}'.format(""),end="")

      print("")

#while
condition = 10
while condition != 0:
      print(condition)
      condition = condition - 1
