print("\nPALINDROME CHECKER FOR ALF\n")

# Get the word/s to be checked from the user
user_input = input("Enter a word/s to check: ")
# Convert the input to lowercase for uniformity 
word = user_input.lower()

# Check if the input word is a palindrome using the string reversal
reverse = word[::-1]

# Check if the input word is a palindrome
if word == reverse :
    # If the input word is a palindrome, display the message v
    print("The word '%s' is a palindrome." % (user_input))
else :
    # If the input word is NOT a palindrome, display the message v
    print("The word '%s' is NOT a palindrome." % (user_input))

