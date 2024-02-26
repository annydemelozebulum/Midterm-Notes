#Asssume operations are executed in order. What is the result of each print

# 1. Assign values to variables a, b, and c
a = 2
b = 3
c = "abc"

# 2. Print values of variables a, b, and c separated by space
print(a, b, c)
# Output: 2 3 abc

# 3. Print values of variables a, b, and c separated by comma
print(a, b, c, sep=",")
# Output: 2,3,abc

# 4. Increment the value of variable a by 2
a += 2

# 5. Check if variable a is equal to 5 and print the result
print(a == 5)
# Output: True

# 6. Print the string c repeated a - b times
print(c * (a - b))
# Output: abcabc

# 7. Find the index of the first occurrence of character "b" in string c
d = c.find("b")

# 8. Print the value of variable d
print(d)
# Output: 1

# 9. Print the result of logical AND operation between d and b
print(d and b)
# Output: 3

# 10. Check if d is equal to True and print the result
print(d == True)
# Output: False

# 11. Concatenate values of variables a, b, c, and d as strings
e = str(a) + str(b) + str(c) + str(d)

# 12. Print the string e, skipping every second character starting from index 1
print(e[1::2])
# Output: 323

# 13. Concatenate string e with its reverse
print(e + e[::-1])
# Output: 523abc1323cba325abc
