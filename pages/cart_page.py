from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class CartPage(Base):

    url_planshety = "https://store77.net/planshety/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    price_apple_1 = '//*[@id="b_step1"]/div/div[1]/div/div/div[3]/div/div'
    word_apple_1 = '//a[@href="/apple_ipad_2021/planshet_apple_ipad_2021_wi_fi_64gb_seryy_kosmos/"]'
    price_samsung_1 = '//*[@id="b_step1"]/div/div[2]/div/div/div[3]/div/div'
    word_samsung_1 = '//*[@id="b_step1"]/div/div[2]/div/div/div[1]/div/div[2]/div/a'
    sum_price = '//*[@id="b_step1"]/div/div[3]/div[1]/div[2]'

    # Getters

    def get_price_apple_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_apple_1)))

    def get_word_apple_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_apple_1)))

    def get_price_samsung_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_samsung_1)))

    def get_word_samsung_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_samsung_1)))

    def get_sum_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sum_price)))

    # Actions

        # Methods

    def assert_value_planshety(self):
        self.assert_word(self.get_price_apple_1(), "29 680 —")
        self.assert_word(self.get_word_apple_1(), "Планшет Apple iPad 2021 10.2 Wi-Fi 64Gb (Серый космос)")
        self.assert_word(self.get_price_samsung_1(), "68 780 —")
        self.assert_word(self.get_word_samsung_1(), "Планшет Samsung Galaxy Tab S9 FE+ 8/128Gb LTE (Зеленый)")
        self.assert_sum_price(self.price_to_digit(self.get_sum_price().text), self.price_to_digit(self.get_price_apple_1().text), self.price_to_digit(self.get_price_samsung_1().text))







