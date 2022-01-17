# TODO save statistics of counter to a file (date, time, counter)


from random import sample
from time import time


separator = '-' * 47
generator = sample((range(1, 10)), 4)


def string_to_list(sequence):
    numbers = []
    for num in sequence:
        numbers.append(str(num))
    return numbers


def main():
    generated = string_to_list(generator)
    bulls = 0
    cows = 0
    counter = 1
    start = time()

    while True:

        print(separator)
        guess = is_input_suitable()
        # print(separator)

        if guess == ''.join(generated):
            break

        is_there_number(guess, cows, bulls, generated)
        counter += 1

    print(separator)
    final_message(counter)
    end = time()
    timer = (end-start)
    print(f'The game took you {timer} seconds.')


def is_there_number(guess, cows, bulls, generated):
    for index, num in enumerate(guess):
        if num in generated and guess[index] == generated[index]:
            bulls += 1
        elif num in generated:
            cows += 1
    return attempts_messages(cows, bulls)


def attempts_messages(cows, bulls) -> None:
    if cows == 1:
        print(f'Cow: {cows}, Bulls: {bulls}')
    elif bulls == 1:
        print(f'Cows: {cows}, Bull: {bulls}')
    elif cows == 1 and bulls == 1:
        print(f'Cow: {cows}, Bull: {bulls}')
    else:
        print(f'Cows: {cows}, Bulls: {bulls}')


def final_message(counter):
    if counter == 1:
        print(f' WINNER, it took you only {counter} attempt '.center(len(separator), '*'))
        print(f' That is pure luck ;-) '.center(len(separator), '*'))
    elif counter <= 5:
        print(f' WINNER, it took you {counter} attempts '.center(len(separator), '*'))
        print(f' That is fantastic result ;-) '.center(len(separator), '*'))
    elif counter <= 10:
        print(f' WINNER, it took you {counter} attempts '.center(len(separator), '*'))
        print(f' You are a good player '.center(len(separator), '*'))
    else:
        print(f' WINNER, it took you {counter} attempts '.center(len(separator), '*'))
        print(f' You can do better next time ;-) '.center(len(separator), '*'))


def is_input_suitable(enter='Enter a number: '):
    while True:
        guess = (input(enter))
        if input_control(guess):
            return guess
        else:
            print(f'!!! Wrong input !!!'.upper(), '\n'
                  f'Must be 4 numbers, not start with 0 and must be unique')
            print(separator)


def input_control(guess) -> bool:
    return guess.isdigit() \
           and not guess.startswith('0') \
           and (len(guess) == 4) \
           and len(guess) == len(set(guess))


def intro() -> None:
    print('Hi there!')
    print(separator)
    print('I\'ve generated a random 4 digit number for you. \n'
          'Let\'s play a bulls and cows game.')


intro()
main()
