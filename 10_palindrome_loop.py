# Check whether a string is a palindrome using loops.
text = input("Enter the string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

if text.lower() == reversed_text.lower():
    print(f"{text} is palindrome")
else:
    print(f"{text} is not palindrome")
