#Strings
hi = 'Hello'
print(hi[0])
print(hi[1])
print(hi[2])
print(hi[3])
print(hi[4])
print(hi[-1])

#addition
bye = ('Bye')
print(hi+bye)
print(hi+" "+bye)

#multiplication
print(3*bye)

#length
print(len(hi))
print(len(bye))

#printing letters
for letter in hi:
    print(letter)

#slice
str = "Hello World"
print(str[0:5])
print(str[:4])
print(str[4:])
print(str[::-1])

#True and False
hi = "banana"
print(hi=="banana")
print(hi=="Banana")

print("ba" in hi)
print("baN" in hi)

#Methods
sentence = "hello world! my name is john"
print(sentence.capitalize())
print(sentence.center(40))
print(sentence.count(" "))
print(sentence.replace(" ","!"))
print(sentence.split())

# Construction + Alteration
s = "Cat"
print(s[0])

s2 = "R" + s[1:]
print(s2)

#Continuing
template = "Today is %s"
print(template % "Tuesday")

template = "%s I have seen %d %s"
print(template % ("Today", 3, "dogs"))
print(template % ("On monday", 7, "cats"))

# Manipulation
name = "Eric"
age = 74
print(f"Hello", name,"."," You are", age)

#Exercises
hi = "Hello"
who = "World"
print(hi + who[:3] + who[:4])
print(hi + " " + who[:3] + who[:4])
print((hi + who).upper())

print("racecar"[::-1])
print((3*(hi+" ") + 5*(who+",")).replace(","," ").split(" "))

#Exercise: Iterate over a string backwards using while
text = "abcdefg"
i = 0
while i < len(text):
    print(text[len(text)-1-i])
    i += 1