# print("Hello World!")

greeting = 'Hello World'
print(greeting)

# name = input('masukan nama : ')
# print(name)

"""
Ini adalah Block Comment,
Teks ini akan diabaikan oleh Python.
"""

'''
Ini adalah Block Comment,
Teks ini akan diabaikan oleh Python.
'''

# Deklarasi dan inisialisasi TIPE DATA
age = 17
salary = 5000000.0

"""ini tipe integer""" 
print(type(age)) 
# ini float .
print(type(salary))

# ini integer
x = 6
print(type(x))

# ini tipe string
x = "6"
print(type(x))

# Umur = Numbers
# Nama = string
# Complex (Gabungan)
# integer
x = 6
print(type(x))
# float
x = 6.0
print(type(x))
# complex
x = 1+2j
print(type(x))

# tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diuba
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

# Boelan
x = True
print(type(x))

x = False
print(type(x))

# multiline
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

# Indexing kata
x = 'Dicoding'
print(x[0])
# metode indexing dan slicing.
x = 'Dicoding'
print(x[2:])

"""
Output:
coding
"""
# Formatted String
name = "Perseus Evans"
print(f"Hello, nama saya {name}")
 
"""
Output: 
Hello, nama saya Perseus Evans
"""
# %-formatting
name = "Perseus Evans"
print("Nama saya %s" % (name))
 
"""
Output: 
Nama saya Perseus Evans
"""

# str.format()
name = "Perseus Evans"
print("Nama saya {}".format(name))
 
"""
Output: 
Nama saya Perseus Evans
"""

# Tipe List
x = [1, 2.2, 'Dicoding']
print(type(x))

"""
Output: 
<class ‘list’>
"""

x = [1, 'Dicoding', True, 1.0]

print(x[2])

""" 
Output:
True
"""

x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

"""
Output:
['Indonesia', 2.2, 'Dicoding']
"""

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])

"""
Output:
laptop
mouse
microphone
keyboard
"""
# implementasi slicing pada Python.
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']
"""

# Tuple
x = (1, "Dicoding", 1+3j)
print(type(x))

"""
Output:
<class 'tuple'>
"""

x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])

""" 
Output:
program
(5, 'program', (1+3j))
"""

x = (5, 'program', 1+3j)
x[1] = 'Dicoding'

"""
Output:
'tuple' object does not support item assignment
"""

# Set
x = {1,2,7,2,3,13,3}
print(x[0])

"""
Output:
'set' object is not subscriptable
"""

x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

"""
Output:
{1, 2, 3, 7, 13}
<class 'set'>
"""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}

"""

# Dictionary
