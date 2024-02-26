#Write a function that takes the name of a text file as parameter. Print out the 3-letter words that start with “b
def print_b_words(filename):
    try:
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Split the content into words
            words = content.split()

            # Iterate through the words
            for word in words:
                # Check if the word is 3 letters long and starts with "b"
                if len(word) == 3 and word[0] == 'b':
                    print(word)

    except FileNotFoundError:
        print("File not found.")


# Call the function with the filename "text"
print_b_words("text")
