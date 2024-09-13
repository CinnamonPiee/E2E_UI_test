# Saucedemo E2E Test

## Описание
E2E тест для автоматической проверки процесса покупки товара на сайте saucedemo.com. Тест написан на Python с использованием Playwright.

## Установка
1. Клонируйте репозиторий

    ```bash
    git clone
    ```

2. Создайте и активируйте виртуальное окружение

   - Windows
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

   - Linux and MacOS
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Установите зависимости

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

## Запуск
Для запуска теста выполните следующую команду:
- Windows
    ```bash
    python tests/test_purchase.py 
    ```

- Linux and MacOS
    ```bash
    python3 tests/test_purchase.py 
    ```
