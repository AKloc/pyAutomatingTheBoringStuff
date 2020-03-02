def spam(divideBy):
    return 42 / divideBy

def spamWithTry(divideBy):
    try:
       return 42 / divideBy
    except:
        print('OOPS. Bad argument.')
        # This will return "None"


print('What number do you want to divide 42 by?')
divisor = int(input())
retVal = spamWithTry(divisor)
print('Returned value is ' + str(retVal))