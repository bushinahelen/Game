from random import choice

def choose_language():
    while True:
        language = input("Слово на каком языке Вы будете отгадывать? ('english / russian') ").strip().lower()
        if language in ('english', 'russian'):
            return language
        print('Язык должен быть "english" или "russian"')


def select_word(language):
    filename = f'{language}_words.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        word_list = f.readlines()

    return choice(word_list).strip()


print("Добро пожаловать в игру 'Виселица'")
print(" ")
print(
"""Правила игры:
Компьютер загадывает слово. Вы называете буквы по одной.
    Если буква есть в слове - открывается её позиция.
    Если буквы нет - человечек на виселице делает шаг к гибели.
Игра продолжается, пока слово не будет отгадано или человечек не будет повешен.
Счастливых Вам Голодных игр и пусть удача всегда будет с вами!"""
)
print(" ")

hangman = (
r"""
┌───┐
      │
      │
      │
      │
      │
=========
""",
r"""
┌───┐
  │   │
  O   │
      │
      │
      │
=========
""",
r"""
┌───┐
  │   │
  O   │
 /    │
      │
      │
=========
""",
r"""
┌───┐
  │   │
  O   │
 / \  │
      │
      │
=========
""",
r"""
┌───┐
  │   │
  O   │
 /|\  │
      │
      │
=========
""",
r"""
┌───┐
  │   │
  O   │
 /|\  │
 /    │
      │
=========
""",
r"""
┌───┐
  │   │
  O   │
 /|\  │
 / \  │
      │
=========
"""
)

language = choose_language()
word = select_word(language)
underlines = '_' * len(word)
max_wrong = len(hangman)-1
wrong_number = 0
used_letters = []

print(f'\nВам нужно отгадать слово, которое состоит из {len(word)} букв')
print(f'Количество ошибок, которое можно совершить за игру: {max_wrong}')

while underlines != word and wrong_number < max_wrong:
    print('_' * 80)
    print(hangman[wrong_number])
    print(f'Вы уже предлагали буквы: {used_letters}')
    print(f'Совершено ошибок: {wrong_number}')
    print(f'Сейчас слово выглядит так (в нем {len(word)} букв): {underlines}')
    attempt = input('Введите букву: ').strip()
    print('_' * 80)

    if attempt.isalpha():
        if len(attempt) == 1:
            attempt = attempt.lower()    
    
            if attempt in used_letters:
                print('\nВы уже предлагали эту букву')
            else:
                used_letters.append(attempt)

                if attempt in word: 
                    print('\nВерно, эта буква есть в слове')
                    new_word = ''
                    for i in range(len(word)):
                        if attempt == word[i]:
                            new_word += attempt
                        else:
                            new_word += underlines[i]
                    underlines = new_word
                else:
                    print(f'\nБуквы "{attempt}" нет в слове')
                    wrong_number += 1
        else:
            print('\nПожалуйста, введите одну букву')
    else:
            print('\nВведите букву, а не цифру или символ')

    

if wrong_number == max_wrong:
    print(hangman[wrong_number])
    print("""Человечка повесили! Умеешь думать? Подумай в следующий раз!
Из-за тебя невинный человек умер!""")
else:
    print('Вы отгадали! Это была битва не на жизнь, а на смерть, но вы смогли одержать победу!')

print(f'Было загадано слово: {word}')
