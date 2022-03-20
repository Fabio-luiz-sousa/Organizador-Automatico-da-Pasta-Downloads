import os
import shutil

path_original=r'C:\Users\Usuario\Downloads'
path_word=r'C:\Users\Usuario\Downloads\WORD'
path_pdf=r'C:\Users\Usuario\Downloads\PDF'
path_imagens=r'C:\Users\Usuario\Downloads\IMAGENS'
path_others=r'C:\Users\Usuario\Downloads\OUTROS'

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

    for roots,dirs,files in os.walk(path_original):
        for file in files:
            if file.endswith('.docx') or file.endswith('.doc') or file.endswith('.odt') or file.endswith('.pptx'):
                old_file_path=os.path.join(roots,file)
                new_old_file=os.path.join(path_word,file)
                shutil.move(old_file_path,new_old_file)
                print(f'Arquivo {file} movido com sucesso')

move_word()

def move_pdf():
    for roots,dirs,files in os.walk(path_original):
        for file in files:
            if file.endswith('.pdf'):
                old_file_path=os.path.join(roots,file)
                new_old_file=os.path.join(path_pdf,file)
                shutil.move(old_file_path,new_old_file)
                print(f'Arquivo {file} movido com sucesso')

move_pdf()

def move_imagens():
    for roots,dirs,files in os.walk(path_original):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.gif') or file.endswith('.jpg'):
                old_file_path=os.path.join(roots,file)
                new_old_file=os.path.join(path_imagens,file)
                shutil.move(old_file_path,new_old_file)
                print(f'Arquivo {file} movido com sucesso')

move_imagens()

def move_others():
    for roots,dirs,files in os.walk(path_original):
        for file in files:
            if not file.endswith('.docx') and not file.endswith('.doc') and not file.endswith('.odt') and not file.endswith('.pptx') and not file.endswith('.png') and not file.endswith('.jpeg') and not file.endswith('.gif') and not file.endswith('.jpg') and not file.endswith('.pdf'):
                old_file_path=os.path.join(roots,file)
                new_old_file=os.path.join(path_others,file)
                shutil.move(old_file_path,new_old_file)
                print(f'Arquivo {file} movido com sucesso')


move_others()
