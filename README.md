# Internet Technology

## Создание виртуального окружения

Для создания окружения выполните команду:
```
python -m venv .venv
```
Для активации окружения
    (CommandLine):
```
.venv\Scripts\activate.bat
```
    (PowerShell):
```
.venv\Scripts\Activate.ps1
```
Чтобы установить все пакеты выполните:
```
pip install -r requirements.txt

Установите pre-commit:
```
pre-commit install
```

## Запуск приложения

Для запуска приложения выполните команду:

```
python run.py
```

Чтобы получить полный список доступных опций выполните команду:

```
python run.py -h
```

## Инструкции для разработчиков

Запуск приложения для разработки:

```
python run.py -d
```
