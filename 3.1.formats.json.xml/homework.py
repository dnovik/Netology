import json
import xml.etree.ElementTree as ET

file_xml = r'newsafr.xml'
file_json = r'newsafr.json'



def get_text_from_json(file):
    # функция читает файл json и возвращает список слов больше 6 символов

    words = list()
    with open(file, encoding='utf-8') as f:
        news = json.load(f)
        articles_qty = len(news['rss']['channel']['items'])

        for article in range(0, articles_qty):
            text = news['rss']['channel']['items'][article]['description'].split(' ')

            for word in text:
                if len(word) > 6:
                    words.append(word.lower())
        
    return words



def get_text_from_xml(file):
    # функция читает файл xml и возвращает список слов больше 6 символов

    words = []
    tree = ET.parse(file_xml)
    root = tree.getroot()

    for article in range(6, len(root[0])):
        text = root[0][article][2].text.split(' ')

        for word in text:
                if len(word) > 6:
                    words.append(word.lower())

    return words



def get_text_from_file(file):
    # функция проверяет формат файла и вызывает соответствующую функцию чтения файла или возвращает ошибку

    format = file.split('.')[-1]

    if format == 'json':
        return get_text_from_json(file)
    elif format == 'xml':
        return get_text_from_xml(file)
    else:
        print('Неизвестный формат')



def get_word_stat(words):
    # функция возвращает словарь частотности слов на основе текста новостей

    words_stat = dict()
    
    for word in words:
        if word not in words_stat:
            words_stat[word] = 1
        else:
            words_stat[word] += 1

    return words_stat



def get_top_words(file):
    # возвращает список наиболее упоминаемых слов длинною более 6 символов

    text = get_text_from_file(file)
    word_stat = get_word_stat(text)
    rates = sorted(list(set(word_stat.values())), reverse=True)[0:10]


    top_words = {}

    for rate in rates:
        for key, value in word_stat.items():
            if rate == value:
                print(key, value)

get_top_words((file_json))

