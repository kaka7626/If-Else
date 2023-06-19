print('Please enter your password:')
password = input()
if password == 'Forward':
    print('Access Granted!')
elif password == '':
    print('You did not enter your password!')
elif password != 'Forward':
    print('Wrong Password!')
