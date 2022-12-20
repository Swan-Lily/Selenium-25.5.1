import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # Вводим логин
    selenium.find_element(By.ID, 'email').send_keys('Liliashad@mail.ru')
    # Вводим пароль
    selenium.find_element(By.ID, 'pass').send_keys('Samsung1#')
    # Нажимаем на кнопку входа в аккаунт
    selenium.find_element(By.CSS_SELECTOR, 'button[type="submit"]').clicl()
    # Переходим к таблице "Мои питомцы"
    selenium.get('https://petfriends.skillfactory.ru/my_pets')
    # Находим количество строк в таблице
    quantity = WebDriverWait(selenium,
    10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))

    left_info = selenium.find_element(By.XPATH, ('//body/div[1]/div[1]/div[1]'))
    num = left_info.get_attribute('innerText')
    # Из количества строк вычитаем строку шапки таблицы и проверяем наличие числа строк в информации слева
    assert str(len(quantity) - 1) in num



