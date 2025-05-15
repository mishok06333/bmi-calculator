# Базовый образ Python
FROM python:3.9-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файлы
COPY bmi.py .

# Запускаем приложение
CMD ["python", "bmi.py"]

