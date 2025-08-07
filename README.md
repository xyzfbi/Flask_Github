
---

# Flask_Github

[![GitHub](https://img.shields.io/github/license/xyzfbi/Flask_Github)](https://github.com/xyzfbi/Flask_Github)
[![GitHub last commit](https://img.shields.io/github/last-commit/xyzfbi/Flask_Github)](https://github.com/xyzfbi/Flask_Github/commits/main)
[![GitHub stars](https://img.shields.io/github/stars/xyzfbi/Flask_Github?style=social)](https://github.com/xyzfbi/Flask_Github)

Веб-приложение на Flask для получения информации о вашем профиле GitHub через API.

- **Репозиторий:** [xyzfbi/Flask_Github](https://github.com/xyzfbi/Flask_Github)

## Возможности

- 🔍 Получение публичной информации о любом профиле GitHub
- 🌐 Простой и интуитивно понятный веб-интерфейс
- ⚡ Быстрый запуск на Flask
- 💾 Сохранение данных в файл

## Быстрый старт

### Требования
- Python 3.8+
- pip
- GitHub API Token

### Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/xyzfbi/Flask_Github.git
   cd Flask_Github
   ```
2. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows: venv\Scripts\activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Создайте файл `.env` и добавьте строку:
   ```
   API_KEY = <ваш-гитхаб-апи-токен>
   ```
5. Запустите приложение:
   ```bash
   python app.py
   ```

## Структура проекта

```
Flask_Github/
├── app.py                # Главный файл приложения
├── requirements.txt      # Зависимости
├── .gitignore            # Игнорируемые файлы
├── .env                  # API ключ
├── data/                 # Сохранённые данные (resume.txt)
├── src/                  # Логика приложения
├── static/               # Статические файлы (CSS, JS)
├── templates/            # HTML-шаблоны
```

## Запуск

- После запуска приложение будет доступно по адресу: [http://localhost:8080](http://localhost:8080)
- По умолчанию отображается информация о владельце токена. Можно ввести другое имя пользователя для получения его профиля.
- Все данные сохраняются в `data/resume.txt`.

## Вклад

Pull requests и предложения приветствуются! Открывайте issues для обсуждения новых идей или багов.

## Лицензия

Проект распространяется под лицензией MIT.

## Авторы

- [xyzfbi](https://github.com/xyzfbi)

## FAQ

**Q: Для чего нужен этот проект?**  
A: Для быстрого получения и просмотра информации о любом профиле GitHub через удобный веб-интерфейс.

**Q: Как получить GitHub API Token?**  
A: Перейдите в настройки своего GitHub аккаунта, создайте новый Personal Access Token и добавьте его в `.env`.

**Q: Как изменить зависимости?**  
A: После установки новых пакетов выполните:
   ```bash
   pip freeze > requirements.txt
   ```

**Q: Где хранятся полученные данные?**  
A: В файле `data/resume.txt`.

---

_Оригинальный репозиторий: [https://github.com/xyzfbi/Flask_Github](https://github.com/xyzfbi/Flask_Github)_
