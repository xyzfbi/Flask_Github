# Flask_Github

![GitHub](https://img.shields.io/github/license/xyzfbi/Flask_Github)
![GitHub last commit](https://img.shields.io/github/last-commit/xyzfbi/Flask_Github)

Flask_Github - это веб-приложение, разработанное с использованием Flask, которое позволяет получать информацию о вашем профиле на GitHub.

## Возможности

- Получение публичной информации о любом профиле GitHub
- Простой и интуитивно понятный веб-интерфейс
- Построено на Flask

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/xyzfbi/Flask_Github.git
    ```
2. Перейдите в каталог проекта:
    ```bash
    cd Flask_Github
    ```
3. Создайте виртуальную среду и активируйте ее:
    ```bash
    python -m venv venv
    source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
    ```
4. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```
5. Создайте .env файл, и в пишите в него строку:
   ```bash
   API_KEY = <ваш-гитхаб-апи-токен>
   ```


## Использование

1. Запустите приложение Flask:
    ```bash
    python app.py
    ```
2. Откройте ваш веб-браузер и перейдите по адресу `http://localhost:8080/`.

3. Изначально будет показана информация о держателе токена. Вы можете изменять имя пользователя в форме и информация будет обновляться. Все данные сохраняются в файле resume.txt в папке data.

## Чтобы изменить файл с зависимостями пропишите в терминал:
   ```bash
   pip freeze > requirements.txt
   ```
## Вклад

Приветствуются любые вклады! Пожалуйста, откройте проблему или отправьте запрос на вытягивание для любых изменений.

## Контакты

По любым вопросам обращайтесь к [xyzfbi](https://github.com/xyzfbi).

## Благодарности

- Документация по Flask: [Flask](https://flask.palletsprojects.com/)
- Документация по API GitHub: [GitHub API](https://docs.github.com/en/rest)