# https://automatetheboringstuff.com/2e/chapter2/

#ironically incorrectly named file. "elif", not "elseif". Don't forget :s.

print('What''s your name?')
name = input()
print('What''s your age?')
age = int(input())

if name != 'Alice':
    print('Hi, stranger.')
else:
    if age < 12:
        print('No way, kid.')
    elif age > 2000:
        print('Are you a vampire...?')
    elif age > 100:
        print('Sorry, granny.')
    else:
        print('Sup, Alice?')