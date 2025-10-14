import os
import shutil

file_extension = {
    'py': 'Python',
    'json': 'JsonData',
    'html': 'WebSite',
    'css': 'WebSite',
    'db': 'Database',
    'txt': 'Document',
    'xml': 'Document',
    'csv': 'Document',
    'cap': 'CaptureFile'
}


def search(path):
    files = []
    with os.scandir(path) as scaner:
        for each_item in scaner:
            if each_item.is_file():
                files.append(each_item.path)
    return files


def organiser(WhereFrom):
    files = search(WhereFrom)
    print(len(files), 'files found!')
    for file in files:
        if not file.endswith('organiz.py'):
            extension = file.split('.')[-1]
            if extension in file_extension:
                try:
                    directory = file_extension.get(extension)
                    destination = WhereFrom + f'/{directory}'
                    os.mkdir(directory)
                    try:
                        shutil.move(file, destination)
                    except FileExistsError:
                        print('File already exists!')
                except FileExistsError:
                    continue
        else:
            print(f'{extension} not in dirtionary!')


organiser(os.getcwd())
