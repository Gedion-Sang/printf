user_number = int(input('Please provide a number from 2 to 1000: '))
is_prime = True
if user_number >= 2 and user_number <= 1000:
    for i in range(2, user_number):
        if user_number % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(user_number, 'is prime!')
    else:
        print(user_number, 'is not prime!')
else:
    print('Incorrect number!')
