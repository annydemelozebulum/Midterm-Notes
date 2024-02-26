
#Conditional Execution
#IF

#Example 1
number = 9
if number % 2 == 0:
    print(number, "is an even number")
    print("Nothing would be printed if it were odd")

#Example 2
a = 10
b = 5
if a > b:
    print(a, ">", b)
elif a < b:
    print(a, "<", b)
else:
    print(a, "=", b)

#Example 3
if a == b:
    print(a, "=", b)
else:
    if a < b:
        print(a, "<", b)
    else:
        print(a, ">", b)

# Example from the slides
#Given the "gross salary of a person, calculate the "net"
#1. Gross less than 1000, income tax = 10%
#2. Gross less than 2000, income tax = 12%
#3. Gross less than 4000, income tax = 14%
#4. Gross more than 4000, income tax = 18%
#5. If the gross is less than 2000, every child gets a tax cut of 1%
#6. If the gross is more than 2000, every child gets you a tax cut of 0,5%

gross_salary = float(input("Enter the gross salary: "))  # Assuming user inputs the gross salary
children = int(input("Enter the number of children: "))  # Assuming user inputs the number of children

# Calculate income tax based on gross salary
if gross_salary < 1000:
    income_tax = 0.10
elif gross_salary < 2000:
    income_tax = 0.12
elif gross_salary < 4000:
    income_tax = 0.14
else:
    income_tax = 0.18

# Calculate tax cut based on the number of children
if gross_salary < 2000:
    tax_cut_per_child = 0.01
else:
    tax_cut_per_child = 0.005

# Calculate net salary
net_salary = gross_salary * (1 - income_tax - (children * tax_cut_per_child))

print("Net salary:", net_salary)

