from random import choice


def RunGame():
    word: str = choice(['apple', 'banana', 'random'])
    guessed: str = ''
    tries: int = 3

    while tries > 0:
        blank: int = 0

        print('word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blank += 1

        if blank == 0:
            print('\n[+]you got it!')
            break

        guess: str = input('\nEnter a letter: ').lower()

        if len(guess) > 1:
            print("[!] Not allow multiple letter at the same time!")
            continue

        if guess in guessed:
            print('[!] You already use the letter!')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'[!] Sorry that was wrong! ({tries} tries remaining)')

            if tries == 0:
                print('[!] You loss the game!')


if __name__ == '__main__':
    RunGame()
