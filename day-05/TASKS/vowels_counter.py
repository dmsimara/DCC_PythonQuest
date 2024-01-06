print("\nVOWEL COUNTER FOR ALF\n")

# get user input for a word/s to check for vowels
user_input = input("Enter a word/s to check: ")
# convert the input to lowercase to ensure uniform counting of vowels
word = user_input.lower()

vowels = 'aeiou'
vowels_count = 0

# to count the number of vowels in the word/s provided by the user
for char in word:
    if char in vowels :
        vowels_count += 1

# display the output/ sum of vowels_count
print("The number of vowels in '%s' is: %d" % (user_input, vowels_count))



