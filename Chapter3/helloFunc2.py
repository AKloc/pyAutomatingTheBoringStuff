def hello(name):
    print('Hello, ' + name)

def helloReturnString(name):
    retVal = 'Hello' + ', ' + name + '. From returnstring.'
    return retVal

print('Enter your name.')
name = input()
hello(name)

print(helloReturnString(name))