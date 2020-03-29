# a loop to get user input until `q` is entered
input_chr = ""
correct_answer = "q"
i = 0
while input_chr.lower() != correct_answer:
    input_chr = input ("Please enter a character >  ")
    i = i + 1
print("Well done, after ",i," try, you found the correct answer...")

