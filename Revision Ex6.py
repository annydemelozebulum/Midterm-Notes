#Write a function that forces the user to enter a multiple of 6 number.
# Use try,except to catch invalid inputs. Return that number


def get_multiple_of_six():
    while True:
        try:
            number = int(input("Please enter a multiple of 6: "))
            if number % 6 == 0:
                return number
        except ValueError:
            pass
        print("Invalid input. Please enter a multiple of 6.")

# Example usage:
result = get_multiple_of_six()
print("The multiple of 6 you entered is:", result)









