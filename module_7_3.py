import string


class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем названия файлов в атрибут
        self.file_names = file_names

    def get_all_words(self):
        # Словарь для хранения слов из файлов
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Считываем содержимое файла
                    content = file.read().lower()

                    # Убираем пунктуацию
                    for symbol in punctuation:
                        content = content.replace(symbol, '')

                    # Разбиваем текст на слова
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []  # Если файл не найден, записываем пустой список

        return all_words

    def find(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        result = {}
        word_lower = word.lower()

        for name, words in all_words.items():
            # Ищем первое вхождение слова
            if word_lower in words:
                result[name] = words.index(word_lower) + 1  # Номер слова в списке (с 1)
            else:
                result[name] = None  # Слово не найдено

        return result

    def count(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        result = {}
        word_lower = word.lower()

        for name, words in all_words.items():
            # Считаем количество вхождений слова
            result[name] = words.count(word_lower)

        return result


# Использование
if __name__ == "__main__":
    # Создаем объект WordsFinder
    finder2 = WordsFinder('test_file.txt')

    # Вывод всех слов
    print(finder2.get_all_words())

    # Нахождение позиции слова
    print(finder2.find('captain'))

    # Подсчет количества слова
    print(finder2.count('captain'))