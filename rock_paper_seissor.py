from random import choice


def WhoPlay(func):
    def wrapper(*args, **kwargs):
        name = input('Enter your name: ')
        psk = input('Enter your passcode: ')
        if psk != "nopasscode":
            print('wrong passcode!')
            quit()
        func(*args, **kwargs)
    return wrapper


@WhoPlay
def main():
    player = input('[R]ock, [P]aper, [S]eissor').lower()
    computer = choice(["r", "p", "s"])
    print(player, 'vs', computer)


main()
