Команды по миграции:

python manage.py makemigrations photos

python manage.py makemigrations accounts

python manage.py migrate

Команда для запуска приложения:

python manage.py runserver

Установка пакетов для работоспособности:

pip install -r requirements.txt

Устанавливать пакеты необходимо в виртуальном окружении:

venv/Scripts/activate, или activate:

Запросы в POSTMAN:

На все запросы необходима авторизация

http://127.0.0.1:8000/api/login/ - Войти для того чтобы получить токен с помощью которого можно отправлять запросы от лица юзера
метод POST, данные: "username", "password" вот пользователи: Ник: John, root, пароль: John, root,

http://127.0.0.1:8000/api/photos/ - Вывод всех фотографий, метод GET

http://127.0.0.1:8000/api/photos/1/ - Вывод одной фотографии, метод GET

http://127.0.0.1:8000/api/photos/1/update/ - Редактирование фотографии при авторизации, метод PUT, данные: "author", "signature"

http://127.0.0.1:8000/api/photos/3/delete/ - Удаление фотографии при авторизации, метод DELETE

http://127.0.0.1:8000/api/photos/create/ - Создание фотографии при авторизации, метод POST, данные: "description"

http://127.0.0.1:8000/api/photos/1/to-favorite/ - Добавление фотографии в избранное, а также снятие с избранного при повторной отправке, метод POST