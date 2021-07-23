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

# operator precedence pemdas
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
string = 'I am a Python based hamster'
stringI = 'I am a Python based hamster'
string[0]
print(string[0])
print(string[-1])
# len is the .length of Bredan Eich's world 
print(len(string))
# way slicker than substrings, slices, splices, etc. imo
print(string[5:11])
print(string[:27])
# concatenation is the same, but type conversion isn't the same
print(2 * string)
word = "Ford"
word = "L" + word[1:]
print(word)
print('word', word);

