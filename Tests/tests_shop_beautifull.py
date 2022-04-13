# командная строка в терминале
# python -m Tests.tests_shop_beautifull
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from selenium.webdriver.chrome.service import Service


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/driver/chromedriver.exe')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test01_login_invalid(self):
        "Ввод неверного логина"
        driver = self.driver
        driver.get('https://beauti-full.ru/')

        login = LoginPage(driver)
        login.click_link_login()
        login.enter_username('fox@yandex.ru')
        login.enter_password('Testtest2022')
        login.click_login()
        time.sleep(3)
        login.click_link_entrance_xpath()
        time.sleep(3)
        login.check_invalid_username_message()
        message_1 = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/div').text
        self.assertEqual(message_1, 'Неверные логин или пароль')

    def test02_password_invalid(self):
        "Ввод неверного пароля"
        driver = self.driver
        driver.get('https://beauti-full.ru/')

        login = LoginPage(driver)
        login.click_link_login()
        login.enter_username('fox-cherry@yandex.ru')
        login.enter_password('Testtest')
        login.click_login()
        time.sleep(3)
        login.click_link_entrance_xpath()
        time.sleep(3)
        login.check_invalid_password_message()
        message_2 = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/div').text
        self.assertEqual(message_2, 'Неверные логин или пароль')

    def test03_username_password_invalid(self):
        "Ввод неверного логина и пароля"
        driver = self.driver
        driver.get('https://beauti-full.ru/')

        login = LoginPage(driver)
        login.click_link_login()
        login.enter_username('fox@yandex.ru')
        login.enter_password('Testtest')
        login.click_login()
        time.sleep(3)
        login.click_link_entrance_xpath()
        time.sleep(3)
        login.check_invalid_username_and_password_message()
        message_3 = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/div').text
        self.assertEqual(message_3, 'Неверные логин или пароль')

    def test04_login_valid(self):
        "Ввод верного логина и пароля. Успешная авторизация"
        driver = self.driver
        driver.get('https://beauti-full.ru/')

        login = LoginPage(driver)
        login.click_link_login()
        login.enter_username('fox-cherry@yandex.ru')
        login.enter_password('Testtest2022')
        login.click_login()

    def test05_click_new_products(self):
        "Проверка кликабельности закладки 'Новинки'"
        driver = self.driver
        driver.get('https://beauti-full.ru/')

        homepage = HomePage(driver)
        homepage.click_new_products()
        message_5 = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[8]/div/div[2]/h1').text
        self.assertEqual(message_5, 'НОВИНКИ')

    def test06_click_women(self):
        "Проверка кликабельности закладки 'Женщинам'"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_women()
        message_6 = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[8]/div/div[2]/h1').text
        self.assertEqual(message_6, 'ЖЕНЩИНАМ')

    def test07_click_large_sizes(self):
        "Проверка кликабельности закладки 'Большие размеры'"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_large_sizes()
        message_7 = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[8]/div/div[2]/h1').text
        self.assertEqual(message_7, 'ЖЕНЩИНАМ. БОЛЬШИЕ РАЗМЕРЫ')

    def test08_click_men(self):
        "Проверка кликабельности закладки 'Мужчинам'"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_men()
        message_8 = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[6]/div/div[2]/h1').text
        self.assertEqual(message_8, 'МУЖЧИНАМ')

    def test09_click_for_children(self):
        "Проверка кликабельности закладки 'Детям'"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_for_children()
        message_9 = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[8]/div/div[2]/h1').text
        self.assertEqual(message_9, 'ДЕТЯМ')

    def test10_click_home(self):
        "Проверка кликабельности закладки 'Дом'"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_home()
        message_10 = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[8]/div/div[2]/h1').text
        self.assertEqual(message_10, 'ДОМ')

    def test11_click_brands(self):
        "Проверка кликабельности закладки 'Бренды'"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_brands()
        message_11 = driver.find_element(By.XPATH, '//*[@id="content-page"]/div/div[2]/div/h1').text
        self.assertEqual(message_11, 'БРЕНДЫ')


    def test12_click_sale(self):
        "Проверка кликабельности закладки 'Распродажа'"
        driver = self.driver


        homepage = HomePage(driver)
        homepage.click_sale()
        message_12 = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[8]/div/div[2]/h1').text
        self.assertEqual(message_12, 'МЕГА-СКИДКИ НА ТОВАРЫ В ИНТЕРНЕТ-МАГАЗИНЕ BEAUTI-FULL.RU')


    def test13_click_personal_account(self):
        "Проверка кликабельности закладки 'Личный кабинет'"
        driver = self.driver


        homepage = HomePage(driver)
        homepage.click_personal_account()
        message_13 = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[6]/div[1]/div/h2').text
        self.assertEqual(message_13, 'ЛИЧНЫЙ КАБИНЕТ')

    def test14_click_basket(self):
        "Проверка кликабельности закладки 'Корзина'"
        driver = self.driver
        driver.get('https://beauti-full.ru/')

        homepage = HomePage(driver)
        homepage.click_basket()
        message_14 = driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[5]/div/div/h1').text
        self.assertEqual(message_14, 'В КОРЗИНУ НИЧЕГО НЕ ДОБАВЛЕНО')

    def test15_search_value(self):
        "Проверка наличия  поля 'Поиск' на сайте"
        driver = self.driver

        message_15 = driver.find_element(By.ID, 'search-field-container').is_displayed()
        self.assertEqual(message_15, True)

    def test16_click_link_ok(self):
        "Проверка корректности кнопки с ссылкой на группу в Одноклассниках"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.move_link_ok()

        link_from_shop_page = driver.find_element(
            By.XPATH, '//*[@id="mm-0"]/div[13]/div/div[1]/div[4]/div[3]/div[1]/a').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)
        #тест падает, так как url в коде(DevTools) не соответствует url в новом окне при клике
        # при этом страница магазина в соц сети открывается

        driver.close()

    def test17_click_link_vk(self):
        "Проверка корректности кнопки с ссылкой на группу в ВК"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.move_link_vk()

        link_from_shop_page = driver.find_element(
            By.XPATH, '//*[@id="mm-0"]/div[13]/div/div[1]/div[4]/div[3]/div[2]/a').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test18_click_link_facebook(self):
        "Проверка корректности кнопки с ссылкой на группу в FB"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.move_link_facebook()

        link_from_shop_page = driver.find_element(
            By.XPATH, '//*[@id="mm-0"]/div[13]/div/div[1]/div[4]/div[3]/div[3]/a').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test19_click_link_instagram(self):
        "Проверка корректности кнопки с ссылкой на группу в Инстаграм"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.move_link_instagram()

        link_from_shop_page = driver.find_element(
            By.XPATH, '//*[@id="mm-0"]/div[13]/div/div[1]/div[4]/div[3]/div[4]/a').get_attribute('href')
        driver.switch_to.window(driver.window_handles[1])
        link_social_media_after_click = driver.current_url

        self.assertEqual(link_from_shop_page, link_social_media_after_click)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    def test20_click_map_site(self):
        "Проверка кликабельности ссылки 'Карта сайта'"
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_map_site()
        message_20 = driver.find_element(By.XPATH, '//*[@id="content-page"]/div/div[2]/h1').text
        self.assertEqual(message_20, 'КАРТА САЙТА')
























    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')

if __name__ == '__main__':
    unittest.main()











