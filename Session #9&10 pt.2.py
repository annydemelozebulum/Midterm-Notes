#Lists

#Basic Examples
a = []
print(a)

a = [1, 3, 5, 2, 54]
print(a)

a = ["me", "myself", "eye"]
print(a)

a = ["me", 2+3, "hey"+"you", -4.2, None]
print(a)

#Backend Operator
lst = [1, 3, 5, 7, 9]
print(lst[1])

lst[1] = 11
print(lst)

lst[1] = lst[2]
print(lst)

#Slicing Lists
list = [1,2,3,4,5,6,7,8,9,10]

print(list[1:3])

print(list[:4])

print(list[4:])

print(list[::3])

print(list[::-1])

#Methods
#Addition append()
t = ["a", "b", "c"]
t.append("d")
print(t)

#Unifying Lists
t1 = ["a", "b"]
t2 = ["c", "d"]
t1.extend(t2)
print(t1)

#Order: lower to high
t1 = ["e", "b", "a", "d", "c"]
t1.sort()
print(t1)

#Removal
#Pop()
t1 = ["a", "b", "c", "d"]
x = t.pop(1)
print(t)
print(x)

#Remove()
t1 = ['a', 'b', 'c', 'd']
t1.remove('b')
print(t1)






