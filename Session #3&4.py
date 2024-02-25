
#Determining type of expressions

#For each of the following expressions indicate the type of expression
#(int, float, bool, NoneType". Use type() to check

print(type(2))        # int
print(type(2.3))      # float
print(type(False))    # bool
print(type(None))     # NoneType
print(type(4*2))      # int
print(type(4/2))      # float
print(type(3.0*1.0))  # float
print(type(~3))       # int
print(type(3 | 2))    # int
#print(type(3 | 2.0))  # float
print(type("xx"))     # str


#For each of the following expressions, indicate the value returned

# Expression 1
print(5 + 2 - 9)

# Expression 2
print(2 + 3 * 5)

# Expression 3
print(--5)

# Expression 4
try:
    print(None + 7)
except TypeError as e:
    print("TypeError:", e)

# Expression 5
print(not None)

# Expression 6
print(4/2)

# Expression 7
print(3.0*1.0)

# Expression 8
print(2 ** 3 + 1)

# Expression 9
print(2 < 3 < 1)

# Expression 10
print(3 > (0**0 * 4))

# Expression 11
try:
    print(2 > 1 and 5)
except SyntaxError as e:
    print("SyntaxError:", e)



