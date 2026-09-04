# Palindrome Checker

text = input("Enter a word or sentence: ")

# Normalize the input
text = text.lower().replace(" ", "")

# Check palindrome
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")