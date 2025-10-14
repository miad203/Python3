import os
import shutil 



def create_folder(path, extension):
	folder_name: str = extension[1:]
	folder_path: str = os.path.join(path, folder_name)
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)

	return folder_path


def sort_files(source_path):
	for root, sub, filenames in os.walk(source_path):
		for filename in filenames:
			filepath: str = os.path.join(root, filename)
			extension: str = os.path.splitext(filename)[1]

			if extension:
				target_folder: str = create_folder(source_path, extension)
				target_path: str = os.path.join(target_folder, filename)
				shutil.move(filepath, target_path)

def remove_empty_folder(source_path):
	for root, sub, filenames in os.walk(source_path, topdown=False):
		for current_dir in sub:
			folder_path = os.path.join(root, current_dir)

			if not os.listdir(folder_path):
				os.rmdir(folder_path)


def main():
	# user_input: str = input('Enter a folder path to sort: ')
	user_input: str = os.getcwd()

	if os.path.exists(user_input):
		sort_files(user_input)
		remove_empty_folder(user_input)
		print('Successfully sorted!')
	else:
		print('Please provide a valid path!')


if __name__ == "__main__":
	main()
	
