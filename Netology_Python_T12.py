"""Программа по поиску фрагмента текста в наборе файлов."""
import os

import maratag as MG


def find_files(files_dir, files, word):
    """Функция по поиску файлов, содержащих строку."""
    locate_files = list()
    for item in files:
        if item[-3:].lower() == 'sql':
            search_file = MG.Newsfile(os.path.join(files_dir, item), 'txt')
            if search_file.find_word(word):
                locate_files.append(item)
    return locate_files


def print_locate_files(files):
    """Функция по выводу списка найденных файлов."""
    for item in files:
        print(os.path.join('Migrations', item))
    print('Всего {}'.format(len(files)))


def main():
    """Инициализация выполнения программы."""
    word = None
    files_dir = os.path.join(os.getcwd(), 'Migrations')
    files = os.listdir(files_dir)

    while True:
        word = input('Введите строку (слово ''выход'' - закончить):').strip()
        if word == 'выход':
            break
        files = find_files(files_dir, files, word)
        print_locate_files(files)
        if len(files) <= 1:
            break


main()
