import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'



def translator(from_lang, to_lang, source_file, destination_file):
    # главная функция, которая уточняет необходимые данные и возвращает перевод

    from_lang_id = get_lang_id(from_lang)
    to_lang_id = get_lang_id(to_lang)

    
    translation = translate_text(source_file, from_lang_id, to_lang_id)
    write_translation(translation, destination_file)



def get_lang_id(language_name):
    # функция принимает название языка на русском и возвращает его параметр в виде id

    langs_url = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'

    params = {
    'key' : API_KEY,
    'ui' : 'ru'
    }

    langs = requests.get(langs_url, params).json()

    lang_dict = langs['langs']

    for lang_id, lang_name in lang_dict.items():
        if language_name == lang_name:
            response = lang_id
            break
        else:
            response = 'Язык не найден'
    
    return response



def translate_text(source_file, from_lang_id, to_lang):
    # функция принимает на вход файл с исходным текстом и передает его на API для перевода
    
    translate_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    
    with open(source_file) as file:
        
        text = file.read()
        
        params = {
            'key' : API_KEY,
            'text' : text,
            'lang' : {from_lang_id : to_lang},
            'format' : 'plain'
        }
    
        response = requests.get(translate_url, params).json()
        translation = response['text'][0]
        
    return translation



def write_translation(translation, destination_file):
    # функция принимает на вход перевод и путь для записи файла
    
     with open(destination_file, 'w', encoding='utf-8') as file:
            file.write(translation)



translator()