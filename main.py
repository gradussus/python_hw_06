import os
import re
import shutil
import sys
from pathlib import Path

def walk (path, level=1):

    # print('Level =', level,'  --------    ', 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            walk(path + '\\' + i, level + 1)
            # print('Спускаемся', path + '\\' + i)
            # print('Возвращаемся в', path)

    # os.chdir(path)

    # list_dir = list(filter(os.path.isdir, os.listdir()))
    # print(os.getcwd())
    # print(list_dir)

    # for p in list_dir:
    #     print(list_dir)
    #     # print(list_dir)
    #     print(p)
    #     walk(p)

    # os.chdir(list_dir[0])
    # print(list_dir)




walk(r'C:\Users\shevc\Desktop\XXX')






# def transliteration (text):

#     dict = {

#         'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
#         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
#         'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
#         'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
#         'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
#         'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
#         'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
#         'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
#         'Ю': 'YU', 'Я': 'YA', 'Ї': 'YI', 'ї': 'yi', 'Є': 'YE', 'є': 'ye'
#     }
#     newName = ''
#     for letter in text:
#         if re.match(r'[a-zA-Z0-9.]', letter):
#             newName += letter
#         elif letter in dict:
#             newName += dict[letter]
#         else:
#             newName += '_'
#     return newName


# def handle_files(starting_directory):
#     init_path = Path(starting_directory)
#     return


# def goClean(args):
#     if len(args) != 2:
#         return
#     else:
#         handle_files(args[1])

# goClean(sys.argv)
