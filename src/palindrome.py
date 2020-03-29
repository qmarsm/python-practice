def ispalindrome(word):
    return word == word[::-1]


# Code body
word = input("Please enter a string to check whether it is Palindrome or not >  ")
fun_return = ispalindrome(word.lower())
if fun_return == True:
    print("It is a Palindrome string...")
else:
    print("Unfortunately it isn't a Palindrome string...")

