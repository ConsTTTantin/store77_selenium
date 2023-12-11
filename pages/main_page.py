import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):

    url = 'https://store77.net/'
    login_user = "9060656595"
    password_user = "Stepik-08"
    url_planshety = "https://store77.net/planshety/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_link_authorization = '//a[@class="link_srav"]'  # кнопка входа на форму логина и пароля
    save_word = '//*[@id="login_mod"]/form/div[2]/div/label'  # локатор(Запомнить меня) для подтверждения формы входа
    user_name = '//input[@name="USER_LOGIN"]'  # поле ввода логина
    password = '//input[@name="USER_PASSWORD"]'  # поле ввода пароля
    button_login = '//input[@class="reg_modal_btn frm_but_left"]'  # кнопка входа юзера послле ввода данных
    button_exit = '//a[@class="reg_modal_btn frm_but_right"]'   # кнопка выхода юзера послле ввода данных
    link_kat_planshety = '//a[@class="kat_block block_link kat_planshet_img"]'  # выбор категории планшеты
    word_kat_planshety = '//h1[@class="title_content pages_title_c content_lr_pad"]'  # проверка страницы планшеты
    check_box_apple = '//input[@id="check-4130457317"]'  # выбор чекбокса Apple

    # Getters

    def get_button_link_authorization(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_link_authorization)))

    def get_login_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.save_word)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_button_exit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_exit)))

    def get_link_kat_planshety(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_kat_planshety)))

    def get_word_kat_planshety(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_kat_planshety)))

    def get_check_box_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_apple)))

    # Actions

    def click_button_link_authorization(self):
        self.get_button_link_authorization().click()
        print("Click button link authorization")

    def input_user_name(self, user_name):
        for i in user_name:
            self.get_user_name().send_keys(i)
            time.sleep(0.3)
        print("Input User Name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input Password")

    def click_button_login(self):
        self.get_button_login().click()
        print("Click button login")

    def click_link_kat_planshety(self):
        self.get_link_kat_planshety().click()
        print("Click kat planshety")

    def click_check_box_apple(self):
        self.get_check_box_apple().click()
        print("Click check box apple")

        # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.asser_url(self.url)
        self.click_button_link_authorization()
        self.assert_word(self.get_login_word(), "Запомнить меня") # Проверяем, что открылась форма авторизации
        self.input_user_name(self.login_user)
        time.sleep(3)
        self.input_password(self.password_user)
        self.click_button_login()
        time.sleep(3)
        self.assert_word(self.get_button_exit(), "Выйти") # Проверяем, что залогинились

    def link_planshety(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_link_kat_planshety()
        self.get_current_url()
        self.asser_url(self.url_planshety)
        self.assert_word(self.get_word_kat_planshety(), "Планшеты")  # Проверяем, что открылась форма с планшетами

    def buy_planshety_apple(self):
        self.click_check_box_apple()
