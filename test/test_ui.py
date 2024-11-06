import allure
import pytest   
from selenium import webdriver   
from pages.MainPage import MainPage
from pages.TaskPage import TaskPage  
from pages.ProjectPage import ProjectPage

@allure.id('DIPLOM_1')
@allure.story('Авторизация')
@allure.epic('UI')
@allure.title('Авторизация на сайте через существующую учетную запись')
@allure.severity('critical')
def test_autorization(): 
    with allure.step('Открытие браузера Google'):
        google = webdriver.Chrome()
        main_page = MainPage(google)

    main_page.autorization('anna.koshan1506@gmail.com', 'QPhdH8qJVtYfJAQ')

@allure.id('DIPLOM_2')
@allure.story('Задачи')  
@allure.epic('UI') 
@allure.title('Создание задачи')
@allure.severity('critical')
def test_tasks():
    with allure.step('Открытие браузера Google'):
        google = webdriver.Chrome()
        main_page = MainPage(google)

    main_page.autorization('anna.koshan1506@gmail.com', 'QPhdH8qJVtYfJAQ')
    with allure.step('Создание задачи'):
        with allure.step('Переход во вкладку "Мои задачи"'):
            task_page = TaskPage(google)
            task_page.my_tasks()

        task_page.important_task('Важная задача')

@allure.id('DIPLOM_3')
@allure.story('Задачи')
@allure.epic('UI')
@allure.title('Выполнение задачи')
@allure.severity('critical')
def test_completed_task():
    with allure.step('Открытие браузера Google'):
        google = webdriver.Chrome()
        main_page = MainPage(google)
   
    main_page.autorization('anna.koshan1506@gmail.com', 'QPhdH8qJVtYfJAQ')
    with allure.step('Создание задачи'):
        with allure.step('Переход во вкладку "Мои задачи"'):
            task_page = TaskPage(google)
            task_page.my_tasks()
  
        task_page.important_task('Важная задача')
  
        task_page.completed_task()  

@allure.id('DIPLOM_4')
@allure.story('Проекты')
@allure.epic('UI')
@allure.title('Добавление проекта')
@allure.severity('critical')
def test_addition_project():
    with allure.step('Открытие браузера Google'):
        google = webdriver.Chrome()
        main_page = MainPage(google)
   
    main_page.autorization('anna.koshan1506@gmail.com', 'QPhdH8qJVtYfJAQ')
    with allure.step('Создание проекта'):
        with allure.step('Переход во вкладку "Мои компании"'):
            project_page = ProjectPage(google)
            project_page.my_company()

        project_page.project('Проект10')

@allure.id('DIPLOM_5')
@allure.story('Проекты')
@allure.epic('UI')
@allure.title('Создание колонки в проекте')
@allure.severity('critical')
def test_create_column():
    with allure.step('Открытие браузера Google'):
        google = webdriver.Chrome()
        main_page = MainPage(google)
  
    main_page.autorization('anna.koshan1506@gmail.com', 'QPhdH8qJVtYfJAQ')
    
    with allure.step('Создание колонки в проекте'): 
        with allure.step('Переход в проект'):   
            project_page = ProjectPage(google)
            project_page.into_project()

        project_page.create_column('Колонка')