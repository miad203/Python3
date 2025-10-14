def PasswordChecker(password: str):
    try:
        with open('rockyou.txt', 'rb') as thefile:
            reader = thefile.read().splitlines()[-1]

        for i, each_match in enumerate(reader, start=1):
            if password == each_match.decode('UTF-8'):
                print(f'Password found at {i} line')
                break
    except Exception as error:
        print(error)
        pass


PasswordChecker('opnTvx16')
