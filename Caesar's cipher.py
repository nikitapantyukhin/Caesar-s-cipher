def correct_text(txt, alph):
    for i in txt:
        if i.isalpha() and i not in alph and i not in alph.lower():
            print('Буквы должны быть только одного алфавита.')
            return False

    return True


def encryption(txt, offset, alph):
    encrypt_text = ''
    for i in txt:
        if i in alph.lower():
            encrypt_text += alph[(alph.lower().index(i) + offset) % len(alph)].lower()
        elif i in alph.upper():
            encrypt_text += alph[(alph.upper().index(i) + offset) % len(alph)].upper()
        else:
            encrypt_text += i

    return encrypt_text


def decryption(txt, offset, alph):
    decrypt_text = ''
    for i in txt:
        if i in alph.lower():
            decrypt_text += alph[(alph.lower().index(i) - offset) % len(alph)].lower()
        elif i in alph.upper():
            decrypt_text += alph[(alph.upper().index(i) - offset) % len(alph)].upper()
        else:
            decrypt_text += i

    return decrypt_text


eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
incomplete_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

print('Добро пожаловать в игру. Здесь ты сможешь поиграться с шифром Цезаря, который использовали еще до н.э.')

while True:
    while True:
        choosing_cipher = input('''
Выбери режим. 
1. Зашифровать текст.
2. Дешифровать текст. 
''')
        if choosing_cipher not in ('1', '2'):
            print('Введи 1 или 2')
        if choosing_cipher in ('1', '2'):
            break

    while True:
        shift = input('\nНа сколько будем сдвигать буквы? ')
        if  not shift.isdigit():
            print('Ты ввел не число.')
        else:
            shift = int(shift)
            break

    while True:
        choosing_alphabet = input('''
Какой алфавит будем использовать?
1. Русский.
2. Английский. 
''')
        if choosing_alphabet not in ('1', '2'):
            print('Введи 1 или 2')
        if choosing_alphabet in ('1', '2'):
            break

    if choosing_alphabet == '1':
        incomplete_alphabet = input('\nЕсли хотите использовать букву "Ё" в алфавите, нажмите "Enter": ')

    while True:
        text = input('\nВведи текст: ')
        if choosing_alphabet == '1' and incomplete_alphabet == '':
            if correct_text(text, rus_alphabet):
                break
        elif choosing_alphabet == '1' and incomplete_alphabet != '':
            if correct_text(text, incomplete_rus_alphabet):
                break
        elif choosing_alphabet == '2':
            if correct_text(text, eng_alphabet):
                break

    if choosing_cipher == '1':
        if choosing_alphabet == '1' and incomplete_alphabet == '':
            print(f'\nЗашифрованный текст: {encryption(text, shift, rus_alphabet)}')
        elif choosing_alphabet == '1' and incomplete_alphabet != '':
            print(f'\nЗашифрованный текст: {encryption(text, shift, incomplete_rus_alphabet)}')
        elif choosing_alphabet == '2':
            print(f'\nЗашифрованный текст: {encryption(text, shift, eng_alphabet)}')
    elif choosing_cipher == '2':
        if choosing_alphabet == '1' and incomplete_alphabet == '':
            print(f'\nРасшифрованный текст: {decryption(text, shift, rus_alphabet)}')
        elif choosing_alphabet == '1' and incomplete_alphabet != '':
            print(f'\nРасшифрованный текст: {decryption(text, shift, incomplete_rus_alphabet)}')
        elif choosing_alphabet == '2':
            print(f'\nРасшифрованный текст: {decryption(text, shift, eng_alphabet)}')

    continuation_game = input('\nЕсли хотите выйти, нажмите "Enter", '
                              'для продолжения игры нажмите любую другую клавишу: ')
    if continuation_game == '':
        print('\nПриходи ещё.')
        break
