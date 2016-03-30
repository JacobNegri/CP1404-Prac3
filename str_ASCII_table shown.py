
def main():

    lower = 10
    upper = 50

    numbers = get_number(lower,upper)
    print(numbers)

    ##for i in range(10, 120, 11): # make sure we have integers of different 'length'
    ##print("{} {}".format(i, chr(i)))

def get_number(lower,upper):

    values = input("Enter a number {} , {}".format(lower,upper))
    while not values.isnumeric() or int(values) < int(lower) or int(values) > int(upper):
        values = input("Please Enter a correct set of numbers {} , {}".format(lower,upper))
    return values
main()
