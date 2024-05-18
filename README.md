
<p align="center">
  <img src="https://github.com/Tatarenok/HumanRecognizer_YOLOv8/assets/89196271/edbfa6ff-c73e-406a-94e6-297f6943ee11" alt="Название изображения">
</p>
<p align="center">
   <img src="https://img.shields.io/badge/Language-Python3.10-purple" alt="Language">
   <img src="https://img.shields.io/badge/Language-HTML-blue" alt="Language">
   <img src="https://img.shields.io/badge/Language-CSS-yellow" alt="Language">
   <img src="https://img.shields.io/badge/Language-JS-orange" alt="Language">
   <img src="https://img.shields.io/badge/License-NONE-Lime" alt="License">
</p>

<p align="center">Приложение на базе FastAPI для распознавания людей на видеопотоках с использованием YOLOv8.</p>

## Содержание

- [Введение](#введение)
- [Особенности](#особенности)
- [Установка](#установка)
- [Использование](#использование)
- [Обнаружение в действии](#обнаружениевдействии)
- [Возможные улучшения](#возможныеулучшения)
- [Содействие](#содействие)
- [Лицензия](#лицензия)
- [Разработчики](#разработчики)

## Введение

HumanRecognizer_YOLOv8 - это мощное приложение, предназначенное для распознавания людей на видеопотоках. Используя возможности YOLOv8, этот проект предоставляет эффективное и точное решение для обнаружения людей на заранее записанных видеофайлах.

## Особенности

- **Быстрое и точное**: Использует YOLOv8 для быстрого и точного распознавания людей.
- **Веб-интерфейс**: Основано на FastAPI, предоставляющем удобный веб-интерфейс.
- **Обработка в реальном времени**: Обрабатывает видеокадры в реальном времени.
- **Настраиваемое**: Легко модифицировать параметры и пороги обнаружения.

## Установка

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/Tatarenok/HumanRecognizer_YOLOv8.git
    cd HumanRecognizer_YOLOv8
    ```

2. **Создайте и активируйте виртуальное окружение:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
    ```

3. **Установите необходимые пакеты:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Скачайте веса модели YOLOv8:**
    - Поместите файл `yolov8s.pt` или `yolov8n.pt` в директорию проекта.
   ```python
   model = YOLO("yolov8s.pt") #поменять на model = YOLO("yolov8n.pt"), если нужна yolov8n.pt
   ```

## Использование

1. **Запустите сервер FastAPI:**
    ```bash
    uvicorn main:app --reload --port 5050
    ```

2. **Откройте ваш веб-браузер и перейдите по адресу:**
    ```
    http://localhost:5050
    ```

3. **Загрузите ваш видеофайл** и начните распознавание людей на видеопотоке.
   
    Поменяйте 3 файла с видео в коде fastapiserver.py
  1)
     ```python
     video_cap = cv2.VideoCapture("videos/[ваше_видео.mp4]")
     ```
  2)
     ```python
     def __init__(self):
          self.video = cv2.VideoCapture("videos/[ваше_видео.mp4]")
     ```
  3)
     ```python
     def open_video(self):
          self.video = cv2.VideoCapture("videos/[ваше_видео.mp4]")
     ```

## Обнаружение в действии
![view](https://github.com/Tatarenok/HumanRecognizer_YOLOv8/assets/89196271/8737310e-dd27-4bbc-a8b7-ef229f6c65ca)

Также есть возможности:
- Запуск показа видео
- Делать скриншот видео
- Отключать показ видео
- С помощью изменения в коде простраивать линию для ограничения (представлено на видео выше)

## Возможные улучшения
1. Подключение CUDA ядер.
2. Открытие видеофайлов при нажатии на соответствующую кнопку, расположенную на сайте.

## Содействие

Будем рады вашим вкладом! Пожалуйста, не стесняйтесь отправлять Pull Request.

1. Форкните репозиторий.
2. Создайте новую ветку для вашей функции.
    ```bash
    git checkout -b feature/YourFeature
    ```
3. Закоммитьте ваши изменения.
    ```bash
    git commit -m 'Добавить новую функцию'
    ```
4. Запушьте ветку.
    ```bash
    git push origin feature/YourFeature
    ```
5. Откройте Pull Request.

## Лицензия

Этот проект бесплатен для использования и не содержит какой-либо лицензии.

## Разработчики
- Правка и доработка кода [Tatarenok](https://github.com/Tatarenok)
- Основной шаблон взят у [Whynot46](https://github.com/Whynot46)

