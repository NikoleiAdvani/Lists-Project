# Nikolei Advani, 10/20/2016
# This program creates a list of all the prime numbers up to a number


def getMaxValue():
    """This function takes the user input and creates a list from 2 to that number"""
    max_number = int(input("Please enter maximum number:"))
    list1 = []
    for x in range(2, max_number + 1):
        list1.append(x)
    return list1


def primeNumbers(list1):
    """This function uses the Sieve of Eratosthenes algorithm to create a list of prime numbers and prints it to user"""
    list2 = []
    while len(list1) > 0:
        first_number = list1[0]
        list2.append(first_number)
        for number in list1:
            if number % first_number == 0:
                list1.remove(number)
    print("the list of prime numbers is", list2)


def main():
    """This function calls all of the other functions"""
    list1 = getMaxValue()
    primeNumbers(list1)


main()
