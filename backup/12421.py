# URL для получения списка моделей
import requests

url = 'http://127.0.0.1:1337/v1/models'

# Отправка GET-запроса для получения списка моделей
response = requests.get(url)

# Вывод списка моделей
print(response.json())