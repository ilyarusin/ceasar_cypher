# Шифр Цезаря

direction = input('Вы хотите зашифровать ли дешифровать текст? \n')
while direction != 'зашифровать' and direction != 'дешифровать':
    direction = input('Наберите "зашифровать" или "дешифровать": \n')

alphabet_lang = input('Выберите язык алфавита:  (русский/английский) \n')
while alphabet_lang not in ('русский', 'английский'):
    alphabet_lang = input('Выберите "русский" или "английский" \n')

while True:
    shift = input('Введите какой будет шаг сдвига: \n')
    if not shift.isdigit():
        print('Ошибка при вводе данных')
    else:
        shift = int(shift)
        break

text = input('Введите текст: \n')
while text.isspace() == True:
    print('Ошибка при вводе данных')
    text = input('Введите текст: \n')

if alphabet_lang == 'русский':
    rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    volume_of_alphabet = 32  
elif alphabet_lang == 'английский':
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    volume_of_alphabet = 26

text_result = ''

if direction == 'зашифровать':
    if alphabet_lang == 'русский':
        for symbol in text:
            if symbol.isalpha() and symbol.islower():
                text_result += rus_lower_alphabet[(rus_lower_alphabet.find(symbol) + shift) % volume_of_alphabet]
            elif symbol.isalpha() and symbol.isupper():
                text_result += rus_upper_alphabet[(rus_upper_alphabet.find(symbol) + shift) % volume_of_alphabet]
            else:
                text_result += symbol
    elif alphabet_lang == 'английский':
        for symbol in text:
            if symbol.isalpha() and symbol.islower():
                text_result += eng_lower_alphabet[(eng_lower_alphabet.find(symbol) + shift) % volume_of_alphabet]
            elif symbol.isalpha() and symbol.isupper():
                text_result += eng_upper_alphabet[(eng_upper_alphabet.find(symbol) + shift) % volume_of_alphabet]
            else:
                text_result += symbol

if direction == 'дешифровать':
    if alphabet_lang == 'русский':
        for symbol in text:
            if symbol.isalpha() and symbol.islower():
                text_result += rus_lower_alphabet[(rus_lower_alphabet.find(symbol) - shift) % volume_of_alphabet]
            elif symbol.isalpha() and symbol.isupper():
                text_result += rus_upper_alphabet[(rus_upper_alphabet.find(symbol) - shift) % volume_of_alphabet]
            else:
                text_result += symbol
    elif alphabet_lang == 'английский':
        for symbol in text:
            if symbol.isalpha() and symbol.islower():
                text_result += eng_lower_alphabet[(eng_lower_alphabet.find(symbol) - shift) % volume_of_alphabet]
            elif symbol.isalpha() and symbol.isupper():
                text_result += eng_upper_alphabet[(eng_upper_alphabet.find(symbol) - shift) % volume_of_alphabet]
            else:
                text_result += symbol
print(text_result)



