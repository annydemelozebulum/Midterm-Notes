#Files
#Review in the end
import math

# Functions
print(max("Hello World!"))
print(min("Hello World!"))
print(len("Hello World"))

print(int(3.2))
print(float(7))

#Math Functions
print(math.sin(30/360 * 2 * math.pi))
print(math.sin(45/360 * 2 * math.pi))
print(math.sqrt(2)/2)

#Random Values

import random

for l in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10))

#Random Choices
people = ["John", "Ana", "Jim", "George", "James"]
print(random.choice(people))


#Creating function
def greet(name):
    """
    Input: none
    This function just prints "hello, <name>"
    """
    print('Hello!', str(name).capitalize())

greet("james")

#Function with 3 arguments
def sum_and_multiply(t1, t2, m):
    """
    :param t1: addition number1
    :param t2: addition number 2
    :param m: multiplicator
    :return: prints(t1+t2)*m
    """

    print((t1+t2)*m)
sum_and_multiply(1, 2,3 )

#Function with Return

def sum_and_multiply(t1, t2, m):
    """
    :param t1: addition number1
    :param t2: addition number2
    :param m: multiplicator
    :return: prints (t1+t2)*m
    """
    return (t1+t2)*m

result = sum_and_multiply(1,2,3)
print("(1+2)*3 - 4 = ", result-4)



import random

# Generate 10 random numbers and add them together
total = sum(random.randint(1, 100) for _ in range(10))

# Print the sum
print("Sum of the 10 random numbers:", total)
