"""Программа по поиску фрагмента текста в наборе файлов."""
import os


def find_word(search_file, word):
    """Функция поиска слова в файле."""
    find_word = False
    if search_file.lower().count(word.lower()) > 0:
        find_word = True
    return find_word


def find_files(files_dir, files, word):
    """Функция по поиску файлов, содержащих строку."""
    locate_files = list()
    for item in files:
        if item.endswith('.sql'):
            filename = os.path.join(files_dir, item)
            with open(filename, 'r') as f:
                search_file = f.read()
            if find_word(search_file, word):
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
    script_dir = __file__
    end_of_path_dir = script_dir.rfind('/') + 1
    files_dir = os.path.join(script_dir[:end_of_path_dir], 'Migrations')
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
