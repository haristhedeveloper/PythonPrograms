import re

# Take input from the user
text = str(input("Enter your e-mail: "))

# This line contain pattern which I want 
pattern = r"@gmail.com"

# Match the pattern with input
match = re.search(pattern, text)

# Check if the pattern is found
if match:
    print("Your e-mail is valid")
else:
    print("Not valid")
