# Tvým úkolem bude vytvořit program, který by simuloval hru Bulls and Cows.
# Po vypsání úvodního textu uživateli, může hádání tajného čtyřciferného čísla začít.

# Program bude obsahovat:
# 1. Program pozdraví užitele a vypíše úvodní text -> DONE
# 2. Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0) -> DONE
# TODO 3. Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla,
#    pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky
# TODO 4. Program vyhodnotí tip uživatele

# Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění),
# příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění).
# Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu.
# Tedy 1 bull a 2 bulls (stejně pro cow/cows).

from random import randint

separator = '-' * 47
generator = randint(1000, 9999)
# TODO osetrit, aby cislice z generatoru byly unikatni - to same entry

def intro() -> None:
    print('Hi there!')
    print(separator)
    print('I\'ve generated a random 4 digit number for you. \n'
          'Let\'s play a bulls and cows game.')
    print(separator)


def input_control():
    entry = '1669'
    if entry.isnumeric() and not entry.startswith('0') and (len(entry) == 4):
        return True
    else:
        return False

# intro()
print(input_control())