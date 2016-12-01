# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

# from collections import Counter

def get_the_a(file_name):
    counter = 0
    for letter in file_name:
        if letter.lower() == "a":
            counter += 1
    return counter

print(get_the_a("02.txt"))
