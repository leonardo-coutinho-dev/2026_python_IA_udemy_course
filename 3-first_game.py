import random, datetime

program_state = True
number_of_lives = 10
counter = 0

date_1 = datetime.datetime.now()

while program_state:
    print('## GAME: Guess the number!\n')

    print('** Your goal is to guess the number!\n')

    print('1. Start with 10 lives.')
    print('2. Guess wrong, loose 1 life.')
    print('3. Guess right, earn 1 life.')
    print('4. Number of lives can go beyond 10.')
    print('5. If it reaches 0, it ends.')

    print('\nNumber of lives:\n')
    for i in range(number_of_lives):
        print(f'{i + 1}. * ', end = "")
        if i == (number_of_lives - 1):
            print('')

    number = int(input('\nTry to guess the number (0 - 9)\n'))

    random_number = random.randint(1, 10)

    if number == random_number:
        print('\n-----> Guessed!\n')
        number_of_lives += 1
    else:
        print('\n-----> Wrong number!\n')
        number_of_lives -= 1

    print(f'random_number: {random_number}, number guessed: {number}\n')

    if number_of_lives == 0:
        program_state = False
        print('--------------------> YOU LOST!')
        date_2 = datetime.datetime.now()
        print(f'\nDuration: {date_2 - date_1}')
    else:
        print('--------------------> NEW MATCH\n')


