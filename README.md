# Дипломная работа 
Дипломная работа по автоматизации тестирования сайта https://ru.yougile.com/. Так же было проведено API-тестирование сайта по доступной для пользователей документации

## Установка (Windows 64x)

1. Установить Visual Studio Code
Перейти на официальный сайт приложения https://code.visualstudio.com/. 
На главной странице появляется кнопка Download for Windows для скачивания актуальной версии. 
Скачать текстовый редактор, нажав на кнопку.

2. Установить Pytest 
Перейти на официальный сайт инструмента pip для pytest https://pypi.org/search/?q=pytest.
Выберите подходящий пакет pytest. На текущий момент актуальной версией pytest является версия 8.3.3, перейдите в этот пакет.
Скопировать команду ```pip install pytest``` в верхнем левом углу сайта.
Далее переходим в VS Code на своем компьютере и вставляем команду в терминал.
Чтобы проверить доступность пакета, нужно написать команду ```pytest --version``` и нажать клавишу Enter. В терминале отобразится установленная версия pytest
__Если при выполнении команд__ 
__```pytest --version```__
__и__
__```pytest```__
__у вас возникает ошибка:__
__```cpytest: The term 'pytest' is not recognized as a name of a cmdlet, function, script file, or executable program.```__ 
__```Check the spelling of the name, or if a path was included, verify that the path is correct and try again.```__
__То используйте для работы команды__
__```python -m pytest --version```__
__```python -m pytest```__

3. Установить Selenium
Чтобы установить Selenium, выполните следующую команду в терминале или командной строке:
```pip3 install selenium```
    3.1 Установка браузера и драйвера (опционально)
Для использования Selenium вам также понадобится установить браузер (например, Google Chrome) и соответствующий драйвер (например, ChromeDriver).
Для Google Chrome:
- Скачайте ChromeDriver с официального сайта: [ChromeDriver](https://sites.google.com/chromium.org/driver/).
    - Убедитесь, что версия ChromeDriver соответствует версии вашего браузера.
    - Распакуйте и поместите исполняемый файл ```chromedriver``` в папку, доступную для вашей системы, или в корневую папку проекта.
- Для других браузеров аналогично скачайте соответствующий драйвер.

4. Установить Requests
Переходим на сайт pypi: https://pypi.org/project/requests/.
Копируем команду для установки библиотеки: ```pip install requests```.
Переходим в VS Code, вставляем команду в терминал и вызываем.

5. Установить Allure
Скопируйте команду для подключения:
```pip install allure-pytest```
Откройте терминал и перейдите к рабочей директории
Подключите Allure:
```pip install allure-pytest```
Запустите тесты и укажите путь к каталогу результатов тестирования:
```pytest --alluredir allure-result```
или
```python -m pytest --alluredir allure-result```
Запустите в терминале VS Code команду
```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```
```Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression```
Затем команду
```scoop install allure```
Введите команду ниже — сгенерируется отчет о тестах:
```allure serve allure-result```

## Документация
1. Документацию для Pytest можно почитать по [ссылке](https://docs.pytest.org/en/stable/)
2. Документацию для Requests можно почитать [здесь](https://requests.readthedocs.io/en/latest/)
3. Документацию для Allure можно почитать [здесь](https://allurereport.org/docs/)
4. Документация для тестирования API [YouGile](https://ru.yougile.com/api-v2#/)