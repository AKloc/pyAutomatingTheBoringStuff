spam = 0

while spam < 5:
    print('spam is ' + str(spam))
    spam += 1

print('What''s your name?')
userName = input()
while userName != 'Carol':
    print('Are you sure you''re not a Carol, Carol? What''s your name?')
    userName = input()
    if userName == 'Quit':
        break

print('That''s what I thought.')