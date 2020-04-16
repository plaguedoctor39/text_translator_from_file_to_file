import requests
import config

#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = config.app_key
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(first_file_path, end_file_path, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param first_file_path:
    :param end_file_path:
    :param from_lang:
    :param to_lang:
    :return:
    """

    with open(first_file_path) as f:
        text = ''
        for line in f:
            text += line
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    print(f'Запрос к URL для {first_file_path}')
    json_ = response.json()
    with open(end_file_path, 'a') as end_file:
        end_file.write(f'Переведенный текст файла {first_file_path}\n')
        end_file.write(''.join(json_['text']) + '\n')


if __name__ == '__main__':
    files = ['DE.txt', 'FR.txt', 'ES.txt']
    with open('translated.txt', 'w') as ex:
        ex.write('')
    for file in files:
        current_file_language = file[0] + file[1]
        translate_it(file, 'translated.txt', current_file_language.lower())
