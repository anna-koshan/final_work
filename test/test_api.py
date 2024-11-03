import allure
import requests
import pytest

Base_url = "https://yougile.com/api-v2/"
token = "FUqspdsMBwTweK622epKLnkU2wl9+2UA2oTHz3huenEmz+JVJFMpoh6bwZiqL6A6"
project_id = "39de6855-5156-4408-b6c0-4302a0a60af4"


def get_headers():
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

@allure.story('Проекты')
@allure.epic('API')
@allure.title('Добавление проекта')
@allure.severity('critical')
def test_create_project():
    with allure.step('Тело для создания проекта'):  
        project = {
            "title": "Postman",
            "users": {
                "6feff6f8-4202-4c92-8043-9481d77efef0": "admin"
            }
        }
    with allure.step('Создание проекта'):  
        response = requests.post(f"{Base_url}projects", json=project, headers=get_headers())
    with allure.step('Проверка статус-кода'):  
        assert response.status_code == 201, "Project creation failed."
    with allure.step('Получение ID созданного проекта'):  
        created_project_id = response.json()["id"]
        print(f"Created project ID: {created_project_id}")

@allure.story('Проекты')
@allure.epic('API')
@allure.title('Получение списка проектов')
@allure.severity('critical')
def test_get_projects():
    with allure.step('Получение списка проектов черезе метод "get"'): 
        response = requests.get(f"{Base_url}projects", headers=get_headers())
    with allure.step('Проекта статус-кода'): 
        assert response.status_code == 200, "Failed to get projects."

@allure.story('Проекты')
@allure.epic('API')
@allure.title('Изменение проекта')
@allure.severity('critical')
def test_update_project():
    with allure.step('Удаление проекта'): 
        with allure.step('Тело для удаления проекта'):   
            payload = {
                "deleted": True,
                "title": "Updated Project2",
                "users": {
                    "6feff6f8-4202-4c92-8043-9481d77efef0": "admin"
                }
            }
    with allure.step('Удаление проекта через метод "put"'): 
        response = requests.put(f"{Base_url}projects/{project_id}", json=payload, headers=get_headers())
    with allure.step('Проверка выполнения заполнения (статус-код)'): 
        assert response.status_code == 200, "Project update failed."

@allure.story('Проекты')
@allure.epic('API')
@allure.title('Получение id проекта, проверка статус-кода')
@allure.severity('minor')
def test_get_project_by_id_status_code():
    with allure.step('Получение id проекта'): 
        response = requests.get(f"{Base_url}projects/{project_id}", headers=get_headers())
    with allure.step('Проверка выполнения запроса (статус-код)'): 
        assert response.status_code == 200, "Failed to get project by ID."

@allure.story('Проекты')
@allure.epic('API')
@allure.title('Получение id проекта')
@allure.severity('minor')
def test_get_project_by_id():
    with allure.step('Получение id проекта'): 
        response = requests.get(f"{Base_url}projects/{project_id}", headers=get_headers())
    with allure.step('Проверка выполнения запроса (статус-код)'): 
        assert response.status_code == 200, "Failed to get project by ID."
    with allure.step('Проверка соответствия фактически полученного id проекта с ожидаемым'): 
        assert response.json()["id"] == project_id, "Project ID does not match."