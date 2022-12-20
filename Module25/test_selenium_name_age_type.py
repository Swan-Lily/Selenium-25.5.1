import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/serglilia/Downloads/chromedriver')

@pytest.fixture(autouse=True)
def testing(selenium):

   # Переходим на страницу авторизации
   selenium.get('http://petfriends.skillfactory.ru/login')

   yield

   selenium.quit()

def test_my_pets(selenium):
   selenium.set_window_size(1920, 1080)
   selenium.maximize_window()
   # Вводим email
   selenium.find_element(By.ID,'email').send_keys('Liliashad@mail.ru')
   # Вводим пароль
   selenium.find_element(By.ID, 'pass').send_keys('Samsung1#')
   # Нажимаем на кнопку входа в аккаунт
   selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   driver.implicitly_wait(10)
   # Переходим к таблице "Мои питомцы"
   selenium.get('https://petfriends.skillfactory.ru/my_pets')



   age = selenium.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-of-type(3)')
   names = selenium.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td')
   type = selenium.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td:nth-of-type(2)')

   for i in range(len(age)):
       assert age[i].text != ''
       assert names[i].text != ''
       assert type[i].text != ''