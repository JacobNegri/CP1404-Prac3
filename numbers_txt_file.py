
## opens numbers txt file and adds them together

in_file = open("numbers.txt", "r")

num1 = int(in_file.readline())
num2 = int(in_file.readline())
print(num1 + num2)
in_file.close()
