#Write a function that takes an integer as parameter and returns a list of all thedivisors of that number:
# #ex: 47 -> [1,47], 28 -> [1,2,4,7,14,28]

def find_divisors(number):
    divisors = []  # Initialize an empty list to store divisors

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)  # Append divisor to the list

    return divisors


# Example usage:
print(find_divisors(47))  # Output: [1, 47]
print(find_divisors(28))  # Output: [1, 2, 4, 7, 14, 28]


