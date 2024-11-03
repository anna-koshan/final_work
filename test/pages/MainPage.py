import allure
from selenium.webdriver.common.by import By   
from selenium.webdriver.support import expected_conditions as EC   

class MainPage:
    def __init__(self, google): 
        self._google = google
        google.get('https://ru.yougile.com/')
        google.implicitly_wait(4)   
        google.maximize_window()

    @allure.step('Авторизация через логин и пароль')
    def autorization(self, email, pass_word):
        sign_in = self._google.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()  
        self._google.implicitly_wait(10) 
        self._google.find_element(By.XPATH, "//input[@placeholder='E-mail…']").send_keys(email)  
        password = self._google.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys(pass_word)  
        button_submit = self._google.find_element(By.XPATH, "//div[@role='button']").click()  
        self._google.implicitly_wait(10) 