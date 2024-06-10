# function to call all other functions
def main():
    A, P, t = compound()
    printValue(A, P, t)

# generic function to handle exceptions
def getNum(prompt = 'Enter number: '):
    while True:
        num = input(prompt)
        try:
            num = float(num)
            return num
        except:
            print('Invalid number. Please enter a valid number.')
            

# take user input for values
def compound():
    P = float(getNum('How much are you investing?\n'))
    r = float(getNum('What is the interest rate in %?\n'))
    n = float(getNum('How many times per year is the interest being compounded?\n'))
    t = float(getNum('How many years are you leaving the investment to be compounded?\n'))

# calculate total with interest formula
    A = P * ((1+((r * 0.01)/n)) ** (n * t))
    return A, P, t

# print final value of investment
def printValue(A, P, t):
    string_A = str(round(A, 2))
    string_t = str(t)
    print('After ' + string_t + ' years, you have a total of $' + string_A)

# calculate net gain
    net_gain = A - P
# print net gain
    string_net_gain = str(round(net_gain, 2))
    print('Your net gain is: $' + string_net_gain)

# call main
main()
