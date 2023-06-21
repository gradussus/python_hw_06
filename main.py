import os
import re
import shutil
import sys
from pathlib import Path

known_extensions = {
    'images': ('jpeg', 'png', 'jpg', 'svg'),
    'videos': ('avi', 'mp4', 'mov', 'mkv'),
    'documents': ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'),
    'music': ('mp3', 'ogg', 'wav', 'amr'),
    'archives': ('zip', 'gz', 'tar')
    }

unknown_extensions = set()

def walk (path, init_path):

    for i in os.listdir(path):
        
        # print(i)
        if os.path.isdir(os.path.join(path, i)):
            walk(os.path.join(path, i), init_path)
        else:
            move_file(path, i, init_path)


def move_file(old_folder, filename, init_path ):
    for i in known_extensions:
        print(i)
    

        if filename.endswith(known_extensions[i]):

            old_file = os.path.join(old_folder, filename)

            if not os.path.exists(os.path.join(init_path, i)):
                os.makedirs(os.path.join(init_path, i))

            new_file = os.path.join(init_path, i , transliteration(filename))
            
            os.rename(old_file, new_file)

# walk(r'C:\Users\shevc\Desktop\XXX')


def transliteration (text):

    dict = {

        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
        'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
        'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
        'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
        'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
        'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
        'Ю': 'YU', 'Я': 'YA', 'Ї': 'YI', 'ї': 'yi', 'Є': 'YE', 'є': 'ye'
    }
    newName = ''
    for letter in text:
        if re.match(r'[a-zA-Z0-9.]', letter):
            newName += letter
        elif letter in dict:
            newName += dict[letter]
        else:
            newName += '_'
    return newName


def goClean(args):
    if len(args) != 2:
        print('Enter the desired directory after the script name')
        return
    else:
        walk(args[1], args[1])

goClean(sys.argv)
