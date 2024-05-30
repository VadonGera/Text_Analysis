from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter


# Читаем содержимое файла в байтовом формате и декодируем его в строку с использованием  UTF-8
def load_text(filename):
    try:
        with open(filename, 'rb') as file:  # Открываем файл в режиме чтения в бинарном режиме
            return file.read().decode('utf-8')
    except FileNotFoundError:
        print("Файл не найден.")
        return None


# Очистка текста от цифр, знаков препинания и стоп-слов
def process_text(text):
    tokens = word_tokenize(text)  # Токенизация текста, разбиваем текст на слова
    clean_tokens = clean_text(tokens)  # Приведение к нижнему регистру и удаление знаков препинания и цифр
    stopwords_tokens = remove_stopwords(clean_tokens)  # Исключаем стоп-слова
    return stopwords_tokens


def clean_text(tokens):
    # Приведение к нижнему регистру и удаление знаков препинания
    cleaned_tokens = [token.lower() for token in tokens if token.isalpha()]
    return cleaned_tokens


# Исключаем стоп-слова из списка слов
def remove_stopwords(tokens):
    # Расширяем список стоп-слов для русского языка
    stop_words = stopwords.words('russian') + ['это', 'сказал', 'сказала', 'говорил', 'говорила', 'очень', 'мог']
    return [token for token in tokens if token not in stop_words]


# Подсчет частоты встречаемости слов
def count_words(cleaned_words):
    word_counts = Counter(cleaned_words)  # Создаем словарь с частотой встречаемости слов
    return word_counts


# Получаем наиболее часто встречающихся слов
def get_top_words(word_counts, n=10):
    return word_counts.most_common(n)  # Получаем список самых часто встречающихся слов


def main():
    # Загрузка текста романа
    filename = "content/Толстой Лев. Анна Каренина.txt"
    text = load_text(filename)

    if text:
        cleaned_words = process_text(text)
        word_counts = count_words(cleaned_words)  # Создаем словарь с частотой встречаемости слов

        top_words = get_top_words(word_counts, 10)  # Получаем список самых часто встречающихся слов
        print("Самые часто встречающиеся слова в романе:")
        for word, count in top_words:
            print(f"{word}: {count}")  # Выводим слова и их частоту встречаемости


if __name__ == '__main__':
    main()
