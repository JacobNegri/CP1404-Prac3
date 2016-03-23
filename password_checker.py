
# Constants
SPECIALS = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"
LOWEST_LENGTH = 5
HIGHEST_LENGTH = 15

numbers = 0
upper_case = 0
lower_case = 0
special = 0

password = input("Please enter a password\n Must contain at least one lower case, upper case and special character.")

for character in password:
    if character.islower():
        lower_case += 1
    elif character.isupper():
        upper_case += 1
    elif character.isnumeric():
        numbers += 1
    elif character in SPECIALS:
        special += 1

if len(password) <5:
    print("invalid password")
elif len(password) >15:
    print("invalid password")
elif lower_case <1:
    print("invalid password")
elif upper_case <1:
    print("invalid password")
elif special <1:
    print("invalid password")
elif numbers <1:
    print("invalid password")
else:
    print("valid password accepted, your password is:", password)
