"""Библиотека функций для выполнения домашних заданий."""


import operator

import chardet

import json

class Newsfile(object):
    """Класс - новостной файл."""

    name = None
    encoding = None
    news = ''
    words = None

    def __init__(self, filename, file_format, code_file=None):
        """Объявление класса и чтение файла в аттрибуты экземпляра класса."""
        if file_format == 'txt':
            self.news = self.open_file_txt(filename).decode(self.encoding)
        elif file_format == 'json':
            self.convert_json_txt(self.open_file_json(filename, code_file))
        self.name = filename

    def open_file_txt(self, filename):
        """Открытие файла формата txt."""
        with open(filename, 'rb') as f:
            news = f.read()
            attribs_file = chardet.detect(news)
            self.encoding = attribs_file['encoding']
            return news

    def open_file_json(self, filename, code_file):
        """Открытие файла формата json."""
        with open(filename, encoding=code_file) as f:
            news = json.load(f)
            self.encoding = 'json, ' + code_file
            return news

    def convert_json_txt(self, news):
        """Конвертирование json в txt."""
        for keys in news:
            if type(news[keys]) == type(dict()):
                self.convert_json_txt(news[keys])
            elif type(news[keys]) == type(list()):
                for items in news[keys]:
                    self.news += items['title'] + ' '
                    self.news += items['description'] + ' '

    def count_top(self, n=6):
        """Подсчет количества слов в файле. Определение рейтинга слов."""
        self.words = {}
        our_list = list(self.news.split())
        for item in our_list:
            if len(item.strip()) >= n:
                if self.words.get(item) is None:
                    self.words[item] = 1
                else:
                    self.words[item] += 1
        self.words = sorted(self.words.items(),
                            key=operator.itemgetter(1), reverse=True)

    def print_top(self, top):
        """Вывод топ-рейтинга слов."""
        print('Файл {}, кодировка {}'.format(self.name, self.encoding))
        count = 0
        for key, value in self.words:
            print('Слово: "{}", частота использования: {}'.format(key, value))
            count += 1
            if count == top:
                break
        print('----------')

    def find_word(self, word):
        find_word = False
        if self.news.lower().count(word.lower()) > 0:
            find_word = True
        return find_word
