# страница пользовательского профиля
import time

from selenium.webdriver.common.by import By
from Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.new_products_link_xpath = Locators.new_products_link_xpath
        self.women_link_xpath = Locators.women_link_xpath
        self.large_sizes_link_xpath = Locators.large_sizes_link_xpath
        self.men_link_xpath = Locators.men_link_xpath
        self.for_children_link_xpath = Locators.for_children_link_xpath
        self.home_link_xpath = Locators.home_link_xpath
        self.brands_link_xpath  = Locators.brands_link_xpath
        self.sale_link_xpath = Locators.sale_link_xpath
        self.sale_link_xpath = Locators.sale_link_xpath
        self.personal_account_link_xpath = Locators.personal_account_link_xpath
        self.basket_link_xpath = Locators.basket_link_xpath
        self.link_vk_xpath = Locators.link_vk_xpath
        self.link_ok_xpath = Locators.link_ok_xpath
        self.link_facebook_xpath = Locators.link_facebook_xpath
        self.link_instagram_xpath = Locators.link_instagram_xpath
        self.map_site_link_xpath = Locators.map_site_link_xpath


    def click_personal_account(self):
        self.driver.find_element(By.XPATH, self.personal_account_link_xpath).click()

    def click_new_products(self):
        self.driver.find_element(By.XPATH, self.new_products_link_xpath).click()

    def click_sale(self):
        self.driver.find_element(By.XPATH, self.sale_link_xpath).click()

    def click_basket(self):
        self.driver.find_element(By.XPATH, self.basket_link_xpath).click()

    def click_women(self):
        self.driver.find_element(By.XPATH, self.women_link_xpath).click()

    def click_large_sizes(self):
        self.driver.find_element(By.XPATH, self.large_sizes_link_xpath).click()

    def click_men(self):
        self.driver.find_element(By.XPATH, self.men_link_xpath).click()

    def click_for_children(self):
        self.driver.find_element(By.XPATH, self.for_children_link_xpath).click()

    def click_home(self):
        self.driver.find_element(By.XPATH, self.home_link_xpath).click()

    def click_brands(self):
        self.driver.find_element(By.XPATH, self.brands_link_xpath).click()

    def move_link_ok(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, self.link_ok_xpath).click()
        time.sleep(3)

    def move_link_vk(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, self.link_vk_xpath).click()
        time.sleep(3)

    def move_link_facebook(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, self.link_facebook_xpath).click()
        time.sleep(6)

    def move_link_instagram(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, self.link_instagram_xpath).click()
        time.sleep(5)

    def click_map_site(self):
        self.driver.find_element(By.XPATH, self.map_site_link_xpath).click()
