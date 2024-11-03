import allure
from selenium.webdriver.common.by import By     
from selenium.webdriver.common.keys import Keys

class TaskPage:

    def __init__(self, google):
        self._google = google

    def my_tasks(self): 
        self._google.find_element(By.XPATH, "//body/div/div/div/div/div[7]/div[2]").click()  
        self._google.implicitly_wait(10) 
  
    @allure.step('Создание задачи в разделе "Важные задачи" со сгенерированным названием новой задачи')
    def important_task(self, task_1): 
        self._google.find_element(By.XPATH, '''//div[@class='flex items-center gap-8']//div[3]//*[name()='svg']//*[name()='path' and contains(@d,'M8 3.333v9')]''').click()   
        self._google.implicitly_wait(10) 
        task = self._google.find_element(By.XPATH,"//input[@placeholder='Введите название задачи…']")   
        task.send_keys(task_1)   
        task.send_keys(Keys.ENTER)   
        self._google.implicitly_wait(10) 
        click_to_the_side = self._google.find_element(By.XPATH, '''/html''').click()  
    
    @allure.step('Нажатие на чекбокс для выполнения задачи')
    def completed_task(self): 
        completed = self._google.find_element(By.CSS_SELECTOR, '''#loggedin-container > div.loggedin-below.loggedin-page--my-tasks.appear > div.flex.flex-row.flex-1.h-full > div.cnt-main.z-1.min-w-0.flex-1 > div > div > div.w-full.bg-primary > div.scrollbar-container.ps > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(1) > div.min-w-full > div:nth-child(2) > div > div > div > div:nth-child(2) > div > div > div.h-full.flex.items-center > div > div''').click()    