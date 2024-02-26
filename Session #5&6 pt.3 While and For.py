#Example 1
n = 7
result = 0

while n < 10:
    result += n
    n += 1
print("The sum of the first 9 numbers is", result)

#Example 2
while True:
    num = input("Give me a number (type quit to exit)")
    num2 = input("Give me another number(type quit to exit)")
    if num == "quit" or num2 == "quit":
        break
    num = int(num)
    num2 = int(num2)
    if num2 == 0:
        print("Can not divide by zero")
        continue
    print("The division result of", num, "and", num2, "is", num/num2)

#Exercise
divisor = 3
for num in range(0, 12, 3):
    print(num/divisor)

#Exercise 2
for letter in 'Ahola':print(letter)

#Exercise 3
num = 0
while num <= 5:
    print(num)
    num += 2

print("Out")
print(num)

#Exercise 4
num = 18
count = 0
while num <= 30:
    if num % 3 == 0:
        count += 1
    num += 1

print("Numbers divisible by 3", count)