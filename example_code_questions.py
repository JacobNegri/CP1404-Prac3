
try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator
except ValueError:
 print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
 print("Cannot divide by zero!")
print("Finished.")

# 1. A letter is inputted by the user
# 2. 0 is entered as the denominator
# 3. Add in an IF statement that wont allow zero as an input