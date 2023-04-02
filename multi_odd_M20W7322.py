# Assignment_04_multiplication for every digit situated on the odd spot in the given numbers_M20W7322_Arun
# welcome
def main():
    # import required package
    import re
    string1 = str(input('Enter the numbers'))
    if string1 == 'exit':
        print('Thank you for testing the code and Thank you for the support given by Prof Drdla Matej sir')
        exit()
    else:
        # Function checks if the input string contains any special character or not
        string_check = re.compile('[-+.@_!#$%^&*()<>?/\|}{~:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]')
    # Pass the string in search function
    # of RE object (string_check)
    if (string_check.search(string1) == None):
        # converting string list to integer list
        numbers = [int(i) for i in string1]
        # Checking for odd index
        numbers = numbers[0::2]
        # Avoiding zero in  the list
        numbers = [i for i in numbers if i != 0]
        # Multiplication executing
        mul_result = 1
        for x in numbers:
            mul_result = mul_result * x
        print('The odd number sequence is', numbers, 'and the product of numbers are', mul_result)
        print('Please type >>exit<< in input so that you can stop the program!Thank you')
        return main()
    else:
        print("Please enter positive integers only! without any space,special characters and no float numbers ")


while True:
    # main program
    while True:
        answer = str(input('Hai,please type YES(Y) to start the program and NO(N) to exit(Y/N): '))
        if answer in ('Y', 'N'):
            break
        print("invalid input")
    try:
        if answer == 'Y':
            main()
    except ValueError:
        print('Please avoid square bracket in input!Thanks!')
    else:
     continue
