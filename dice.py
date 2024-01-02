import random

response = 'y'

while response == 'y':
    response = input('What you like to roll the dice (answer y or n): ')
    num = random.randint(1, 6)
    if response == 'y':
        if num == 1:     
            print('[-----] \n[     ] \n[  0  ] \n[     ] \n[-----]')
        elif num == 2:
            print('[-----] \n[0    ] \n[     ] \n[    0] \n[-----]')
        elif num == 3:
            print('[-----] \n[     ] \n[0 0 0] \n[     ] \n[-----]')
        elif num == 4:
            print('[-----] \n[0   0] \n[     ] \n[0   0] \n[-----]')
        elif num == 5:
            print('[-----] \n[0   0] \n[  0  ] \n[0   0] \n[-----]')
        elif num == 6:
            print('[-----] \n[0   0] \n[0   0] \n[0   0] \n[-----]')
        else:
            print('Invalid input!')
    