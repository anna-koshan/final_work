import allure
from selenium.webdriver.common.by import By   
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.support import expected_conditions as EC   

class ProjectPage:

    def __init__(self, google):
        self._google = google

    def my_company(self):
        self._google.find_element(By.XPATH, '//body/div/div/div/div/div/div[4]').click()
        self._google.implicitly_wait(10)
    
    @allure.step('Создание проекта со сгенерированным названием')
    def project(self, project_send):
        self._google.find_element(By.XPATH, "//span[contains(text(),'Добавить проект')]").click()
        WebDriverWait(self._google, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Введите название проекта…']"))).send_keys(project_send)
        self._google.implicitly_wait(10)
        self._google.find_element(By.XPATH, "//div[contains(text(),'Создать проект')]").click()

    def into_project(self):
        WebDriverWait(self._google, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Не удалять! Для проверки!')]"))).click() 
        self._google.implicitly_wait(10)
    @allure.step('Создание колонки')
    def create_column(self, value):
        WebDriverWait(self._google, 10).until(EC.element_to_be_clickable((By.XPATH, './/span[text()[.="Создать колонку"]]'))).click()  
        self._google.find_element(By.XPATH, "//textarea[@placeholder='Введите имя колонки…']").send_keys(value)
        self._google.find_element(By.XPATH, '//*[@id="loggedin-container"]/div[2]/div[2]').click()  
        self._google.implicitly_wait(10)