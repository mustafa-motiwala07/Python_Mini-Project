import re

Password = input("Enter the password here: ")
pattern = "\A(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@%&])[A-Za-z\d@%&]{5,10}$"

x = re.findall(pattern, Password)

if x:
   print("Valid")
else:
   print("Invalid")
