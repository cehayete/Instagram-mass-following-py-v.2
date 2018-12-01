# Instagram-mass-following-py v.2.2
>В версии 2.2 изменился способ настройки - SETTINGS.py

###### Как использовать:
0. Установить библеотеку **InstagramAPI**. Команда для установки через консоль:
```bash
pip install InstagramAPI
```
1. Скачать репозиторий. Команда для установки:
```bash
git clone https://github.com/emilastanov/Instagram-mass-following-py-v.2.git
```
2. Открыть файл **SETTINGS.py** и изменить настройки в соответствии с вашими данными:
```python
username = "username"
password = "password"

run.setDonors(
    'username 1',
    'username 2',
    'username 3',
    	...
    'username N'
)
```
4. Запустить файл **run.py**. Команда для запуска:
```bash
python3 run.py
```
