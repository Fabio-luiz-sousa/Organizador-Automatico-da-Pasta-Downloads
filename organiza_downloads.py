import os
import shutil


path_original = r'C:\Users\Usuario\Downloads'
path_word = r'C:\Users\Usuario\Downloads\WORD'
path_pdf = r'C:\Users\Usuario\Downloads\PDF'
path_imagens = r'C:\Users\Usuario\Downloads\IMAGENS'
path_others = r'C:\Users\Usuario\Downloads\OUTROS'


def create_path():
    if os.path.exists(path_word):
        print('ja existe a pasta WORD nos Downloads')
        return
    elif os.path.exists(path_pdf):
        print('ja existe a pasta PDF nos Downloads')
        return
    elif os.path.exists(path_imagens):
        print('ja existe a pasta IMAGENS nos Downloads')
        return
    elif os.path.exists(path_others):
        print('ja existe a pasta OUTROS nos Downloads')
        return

    os.mkdir(path_word)
    os.mkdir(path_pdf)
    os.mkdir(path_imagens)
    os.mkdir(path_others)


create_path()


def move_word():

    for file in os.listdir(path_original):
        if file.endswith(('.docx', '.doc', '.odt', '.pptx', '.xlsx', '.csv')):
            print(file)
            old_file_path = os.path.join(path_original, file)
            new_path_file = os.path.join(path_word, file)
            shutil.move(old_file_path, new_path_file)


move_word()


def move_pdf():
    for file in os.listdir(path_original):
        if file.endswith('.pdf'):
            print(file)
            old_file_path = os.path.join(path_original, file)
            new_path_file = os.path.join(path_pdf, file)
            shutil.move(old_file_path, new_path_file)


move_pdf()


def move_imagens():

    for file in os.listdir(path_original):
        if file.endswith(('.png', '.jpeg', '.gif', '.jpg', '.ico')):
            print(file)
            old_file_path = os.path.join(path_original, file)
            new_path_file = os.path.join(path_imagens, file)
            shutil.move(old_file_path, new_path_file)


move_imagens()


def move_others():

    for file in os.listdir(path_original):
        if not file.endswith(('.png', '.jpeg', '.gif', '.jpg', '.ico', '.pdf', '.docx', '.doc', '.odt', '.pptx', '.xlsx', '.csv')) and '.' in file:
            print(file)
            old_file_path = os.path.join(path_original, file)
            new_path_file = os.path.join(path_others, file)
            shutil.move(old_file_path, new_path_file)


move_others()
