# Instagram-mass-following-py v.2.1
>В версии 2.1 появилось возможность выбрать режим:
>**IMF.start_loop(mode=value)**
>mode = 1 - Массфоловинг на подписчиков донеров.
>mode = 2 - Подписка и отписка на донеров.

###### Как использовать:
0. Установить библеотеку **InstagramAPI**. Команда для установки через консоль:
```
pip install InstagramAPI
```
1. Скачать репозиторий. Команда для установки:
```
git clone https://github.com/emilastanov/Instagram-mass-following-py-v.2.git
```
2. Создать файл **login.py** в том же каталоге, и поместить в него следующий код:
```
username = "username"
password = "password"
```
3. Отредактировать файл **run.py**:
```
run.setDonors(
    'username 1',
    'username 2',
    'username 3',
    	...
    'username N'
)
```
4. Запустить файл **run.py**. Команда для запуска:
```
python run.py
```