#PYTHON laboratory work 1
#Akhmet Abylay
#PYTHON Introduction
print("Hello, World!")

#PYTHON Syntax
#ex 1
if 5 > 2:
  print("Fe is greater than two!")

#ex 2
if 5 > 2:
 print("Fe is greater than two!") 
if 5 > 2:
        print("Fe is greater than two!")

#ex 3 variables
x = 5
y = "Hello, World!"

#ex 4  Comments
#This is a comment.
print("Hello, World!")

#PYTHON Comments

#ex 1
#This is a comment
print("Hello, World!")

#ex 2
print("Hello, World!") #This is a comment

#ex 3
#print("Hello, World!")
print("Cheers, Mate!")

#ex 4
#This is a comment
#written in
#more than just one line
print("Hello, World!")

#ex 5
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#PYTHONariables

#ex 1
x = 5
y = "John"
print(x)
print(y)

#ex 2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#ex 3 Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

#ex 4
x = 5
y = "John"
print(type(x))
print(type(y))

#ex 5
x = "John"
print(x)
# is the same as
x = 'John'
print(x)

#ex 6
a = 4
A = "Sally"
#A will not erwrite a
print(a)
print(A)

#PYTHON -ariable Names
mar = "John"
myar = "John"
_myar = "John"
mar = "John"
MAR = "John"
mar2 = "John"


print(mar)
print(myar)
print(_myar)
print(mar)
print(MAR)
print(mar2)

#PYTHONariables - Assign Multiples
#ex 1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#ex 2
x = y = z = "Orange"
print(x)
print(y)
print(z)

#ex 3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#PYTHON - Outputariables
#ex 1
x = "PYTHON is awesome"
print(x)

#ex 2
x = "PYTHON"
y = "is"
z = "awesome"
print(x, y, z)

#ex 3
x = "PYTHON "
y = "is "
z = "awesome"
print(x + y + z)

#ex 4
x = 5
y = 10
print(x + y)

#ex 5
x = 5
y = "John"
print(x, y)

#PYTHON - Globalariables
#ex 1
x = "awesome"

def myfunc():
  print("PYTHON is " + x)

myfunc()

#ex 2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("PYTHON is " + x)

myfunc()

print("PYTHON is " + x)

#ex 3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("PYTHON is " + x)

#ex 4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("PYTHON is " + x)

#PYTHON Data Types
#Str #ex 1
x = "Hello World"

print(x)

print(type(x)) 
# Int #ex 2
x = 20
print(x)
print(type(x))

# Float #ex 3
x = 20.5
print(x)
print(type(x))

# Complex #ex 4
x = 1j
print(x)
print(type(x))

# List #ex 5
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))

# Tuple #ex 6
x = ("apple", "banana", "cherry")
print(x)
print(type(x))

# Range #ex 7
x = range(6)
print(x)
print(type(x))

# Dictionary #ex 8
x = {"name": "John", "age": 36}
print(x)
print(type(x))

# Set #ex 9
x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

# Frozenset #ex 10
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# Boolean #ex 11
x = True
print(x)
print(type(x))

# Bytes #ex 12
x = b"Hello"
print(x)
print(type(x))

# Bytearray #ex 13
x = bytearray(5)
print(x)
print(type(x))

# Memoriew #ex 14
x = memoryview (bytes(5))
print(x)
print(type(x))

# None #ex 15
x = None
print(x)
print(type(x))

#Specific Data Type
# String #ex 1
x = str("Hello World")
print(x)
print(type(x))

# Int #ex 2
x = int(20)
print(x)
print(type(x))

# Float #ex 3
x = float(20.5)
print(x)
print(type(x))

# Complex #ex 4
x = complex(1j)
print(x)
print(type(x))

# List #ex 5
x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))

# Tuple #ex 6
x = tuple(("apple", "banana", "cherry"))
print(x)
print(type(x))

# Range #ex 7
x = range(6)
print(x)
print(type(x))

# Dictionary #ex 8
x = dict(name="John", age=36)
print(x)
print(type(x))

# Set #ex 9
x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))

# Frozenset #ex 10
x = frozenset(("apple", "banana", "cherry"))
print(x)
print(type(x))

# Bool #ex 11
x = bool(5)
print(x)
print(type(x))

# Bytes #ex 12
x = bytes(5)
print(x)
print(type(x))

# Bytearray #ex 13
x = bytearray(5)
print(x)
print(type(x))

# Memoryview #ex 14
x = memoryview(bytes(5))
print(x)
print(type(x))

#PYTHON Numbers
#ex 1
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#ex 2 int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#ex 3 float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#ex 4
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#ex 5
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#ex 6
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#ex 7
import random

print(random.randrange(1, 10))

#PYTHON Casting
#ex 1
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

#ex 2
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

#ex 3
x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

#PYTHON Strings
#ex 1
print("Hello")
print('Hello')

#ex 2
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#ex 3
a = "Hello"
print(a)

#ex 4
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#ex 5
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#ex 6
a = "Hello, World!"
print(len(a))

#ex 7
txt = "The best things in life are free!"
print("free" in txt)

#ex 8
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#ex 9 
txt = "The best things in life are free!"
print("expensive" not in txt)

#ex 10
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#PYTHON - Slicing Strings
#ex 1
b = "Hello, World!"
print(b[2:5])

#ex 2
b = "Hello, World!"
print(b[:5])

#ex 3
b = "Hello, World!"
print(b[2:])

#ex 4
b = "Hello, World!"
print(b[-5:-2])

#PYTHON - Modify Strings
#ex 1
a = "Hello, World!"
print(a.upper())

#ex 2
a = "Hello, World!"
print(a.lower())

#ex 3
a = " Hello, World! "
print(a.strip()) 

#ex 4
a = "Hello, World!"
print(a.replace("H", "J"))

#ex 5
a = "Hello, World!"
print(a.split(","))

#PYTHON - String Concatenation
#ex 1
a = "Hello"
b = "World"
c = a + b
print(c)

#ex 2
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#PYTHON - Format - Strings
#ex 1
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#ex 2
price = 59
txt = f"The price is {price} dollars"
print(txt)

#ex 3
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#ex 4
txt = f"The price is {20 * 59} dollars"
print(txt)

#PYTHON - Escape Characters
#ex 1
txt = 'It\'s alright.'
print(txt)

#ex 2
txt = "This will insert one \\ (backslash)."
print(txt) 

#ex 3
txt = "Hello\nWorld!"
print(txt) 

#ex 4
txt = "Hello\rWorld!"
print(txt)

#ex 5
txt = "Hello\tWorld!"
print(txt) 

#ex 6
txt = "Hello \bWorld!"
print(txt)

#ex 7
txt = "\110\145\154\154\157"
print(txt)

#ex 8
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)