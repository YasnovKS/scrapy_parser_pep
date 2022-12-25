# Scrapy parser PEP
### Описание:

Асинхронный парсер документов PEP на базе фреймворка Scrapy. Парсер выводит собранную информацию в два файла .csv:

В первый файл выводит список всех PEP: номер, название и статус.
Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе. В последней строке общее количество всех документов.

### Используемые технологии:

- Python
- Scrapy

### Как запустить проект:

- Клонировать репозиторий на локальную машину
- Cоздать и активировать виртуальное окружение:

Если у вас Linux/MacOS
```Python
    python3 -m venv venv
    source venv/bin/activate
```
Если у вас Windows:
```Python
    python -m venv venv
    source venv/Scripts/activate
```
- Установить зависимости из файла requirements.txt:
```Python
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
### Запуск парсера:
```Python
scrapy crawl pep
```
Файлы будут созданы в дериктории "results"
### Автор проекта:
Кирилл Яснов