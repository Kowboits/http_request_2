import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_header(self):
        header = {'Content-Type' : 'application/json', 'Accept' : 'application/json', 'Authorization' : f'OAuth {self.token}'}
        return header

    def get_upload_url(self, path_to_file):
        upload_link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_header()
        params = {'path' : path_to_file, 'overwrite' : 'True'}
        response = requests.get(upload_link, headers=headers,params=params)
        return response.json()

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        link = self.get_upload_url(path_to_file=file_path).get('href')
        response = requests.put(link, data = open(file_path,'rb'))
        return response
        # Тут ваша логика
        # Функция может ничего не возвращать

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)