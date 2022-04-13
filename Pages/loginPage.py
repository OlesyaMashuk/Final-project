#Страница авторизации
from Locators.locators import Locators
from selenium.webdriver.common.by import By



class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.click_link_login_xpath = Locators.click_link_login_xpath
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_xpath = Locators.login_button_xpath
        self.link_entrance_xpath = Locators.link_entrance_xpath
        self.invalidUsername_message_xpath = Locators.invalidUsername_message_xpath
        self.invalidPassword_message_xpath = Locators.invalidPassword_message_xpath
        self.invalidUsernameAndPassword_message_xpath = Locators.invalidUsernameAndPassword_message_xpath

    def click_link_login(self):
        self.driver.find_element(By.XPATH, self.click_link_login_xpath).click()

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def click_link_entrance_xpath(self):
        self.driver.find_element(By.XPATH, self.link_entrance_xpath).click()

    def check_invalid_username_message(self):
        msg_2 = self.driver.find_element(By.XPATH, self.invalidUsername_message_xpath).text
        return msg_2

    def check_invalid_password_message(self):
        msg_3 = self.driver.find_element(By.XPATH, self.invalidPassword_message_xpath).text
        return msg_3

    def check_invalid_username_and_password_message(self):
        msg_4 = self.driver.find_element(By.XPATH, self.invalidUsernameAndPassword_message_xpath).text
        return msg_4




