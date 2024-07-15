#   String Data types

#   Literal Assignments
first = 'Enoch'
last = 'Mutai'

print(type(first))
print(type(first)== str)
print(isinstance(first, str))

# Contrsuctor function
Pizza = str('pepperroni') 
print(type(Pizza))
print(type(Pizza)== str)
print(isinstance(Pizza, str))

#Concatination
fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

#Casting a number into a string
decade = str(1980)
print(type(decade))
print(decade)
statemenet = "I like rock music from the " + decade +"s!"
print(statemenet)

#Multiple Lines
multiline = '''
Hey, how are you?          
 
I was just checking in.    
                            All good?

'''
print(multiline)

# Escapign special characters 
sentence = 'I\'m back at work! \tHey!\n\nWhere\'s this at\\located?'
print(sentence)

        #String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title()) 
print(multiline.replace("good", "okay")) 
print(multiline)

print(len(multiline))
multiline +="                                "
multiline +="                                "  + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

        #build a menu
title = "menu".upper()
print(title.center(20, "=" ))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheese Cake".ljust(16, ".") + "$4".rjust(4))

print("")

#string index values
print(first[1])
print(first[-1])
print(first[0])
print(first[1:-1])
print(first[1:])

#Some methods return boolean data
print(first.startswith("E"))
print(first.endswith("z"))


#Boolean Data Type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#Numeric Data Types

#Intergre Types
price = 100
bestprice = int(80)
print(type(price))
print(isinstance(bestprice, int))

#Float Type
gpa = 3.28
y=float(1.14)
print(type(gpa))

#Complex Type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#Built-in functions for Numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

#The math module

import math
 
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting a string to a number
zipcode = "00300"
zip_value = int(zipcode)
print(type(zip_value))

#error if you attemot to cast incorrect data
#zip_value = int("New York")