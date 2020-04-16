import requests
import config

token = config.disk_token
URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'


def to_disk(file_path):
    params = {
        'path': file_path,
        'overwrite': True
    }
    headers = {
        'Authorization': token
    }
    response = requests.get(URL, params=params, headers=headers)
    # print(response.headers)
    json_ = response.json()
    # print(json_)
    print(json_)
    files = {'file':open(file_path, 'r', encoding='utf-8')}
    resp = requests.put(json_['href'], files=files)
    if resp.status_code == 201:
        print('Файл успешно загружен')
    else:
        print('Произошла ошибка при загрузке файла')


if __name__ == '__main__':
    to_disk('translated.txt')
