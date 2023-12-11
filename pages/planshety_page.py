import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class PlanshetyPage(Base):

    url_planshety = "https://store77.net/planshety/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    word_kat_planshety = '//h1[@class="title_content pages_title_c content_lr_pad"]'  # проверка страницы планшеты
    check_box_apple = '//label[@for="check-4130457317"]'  # выбор чекбокса Apple
    check_box_samsung = '//label[@for="check-2111568645"]'  # выбор чекбокса Samsung
    produckt_apple_1 = '//*[@id="comp_f82ff9477750d87063add3dcc04f2eb8"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]'  # для наведение на планшет Apple
    price_apple_1 = '//*[@id="comp_f82ff9477750d87063add3dcc04f2eb8"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div[3]/div[1]/p'
    word_apple_1 = '//*[@id="comp_f82ff9477750d87063add3dcc04f2eb8"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div[3]/div[1]/h2/a'
    to_cart_produckt_apple_1 = '//*[@id="comp_f82ff9477750d87063add3dcc04f2eb8"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div[3]/div[3]/div/a/span'  # добавление в карзину apple
    oformlenie_produckta = '//*[@id="modal_add_product"]/div/div/div[3]/div/div'  # проверка добавления в карзину
    select_price_min = '//*[@id="filter_price"]/div/div[1]/input'  # минимальная цена продукта
    produckt_samsung_1 = '//a[@href="/planshety/planshet_samsung_galaxy_tab_s9_fe_8_128gb_lte_zelenyy/"]'  # для наведение на планшет samsung
    price_samsung_1 = '//*[@id="comp_f82ff9477750d87063add3dcc04f2eb8"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div[3]/div[1]/p'
    word_samsung_1 = '//*[@id="comp_f82ff9477750d87063add3dcc04f2eb8"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div[3]/div[1]/h2/a'
    to_cart_produckt_samsung_1 = '//*[@id="comp_f82ff9477750d87063add3dcc04f2eb8"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div[3]/div[3]/div/a/span'  # добавление в карзину samsung
    link_to_cart = '//div[@class="block_basket_login bg_basket"]'   # переход в корзину
    word_cart = '//h1[@class="title_content pages_title_c"]'  # для подтверждения что мы в корзине

    # Getters

    def get_word_kat_planshety(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_kat_planshety)))

    def get_check_box_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_apple)))

    def get_check_box_samsung(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_samsung)))

    def get_produckt_apple_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.produckt_apple_1)))

    def get_price_apple_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_apple_1)))

    def get_word_apple_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_apple_1)))

    def get_produckt_samsung_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.produckt_samsung_1)))

    def get_price_samsung_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_samsung_1)))

    def get_word_samsung_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_samsung_1)))

    def get_to_cart_produckt_apple_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_cart_produckt_apple_1)))

    def get_to_cart_produckt_samsung_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_cart_produckt_samsung_1)))

    def get_oformlenie_produckta(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.oformlenie_produckta)))

    def get_select_price_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_min)))

    def get_link_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_to_cart)))

    def get_word_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_cart)))

    # Actions

    def click_check_box_apple(self):
        self.get_check_box_apple().click()
        print("Click check box apple")

    def click_check_box_samsung(self):
        self.get_check_box_samsung().click()
        print("Click check box samsung")

    def move_produckt_apple_1(self):
        ActionChains(self.driver).move_to_element(self.get_produckt_apple_1()).perform()
        print("Move produckt apple")

    def move_produckt_samsung_1(self):
        ActionChains(self.driver).move_to_element(self.get_produckt_samsung_1()).perform()
        print("Move produckt samsung")

    def click_to_cart_produckt_apple_1(self):
        self.get_to_cart_produckt_apple_1().click()
        print("To cart produckt apple 1")

    def click_to_cart_produckt_samsung_1(self):
        self.get_to_cart_produckt_samsung_1().click()
        print("To cart produckt samsung 1")

    def input_price_min(self, min_price):
        self.get_select_price_min().send_keys(min_price)
        print("Input min price")

    def click_link_to_cart(self):
        self.get_link_to_cart().click()
        print("Link to cart")

        # Methods

    def to_cart_planshety_apple(self):
        self.click_check_box_apple()
        time.sleep(1)
        self.assert_word(self.get_price_apple_1(), "29 680 —")
        self.assert_word(self.get_word_apple_1(), "Планшет Apple iPad 2021 10.2 Wi-Fi 64Gb (Серый космос)")
        self.move_produckt_apple_1()
        time.sleep(1)
        self.click_to_cart_produckt_apple_1()
        self.assert_word(self.get_oformlenie_produckta(), "ОФОРМИТЬ")

    def to_cart_planshety_samsung(self):
        self.click_check_box_apple()
        self.input_price_min(min_price=50000)
        time.sleep(3)
        self.click_check_box_samsung()
        time.sleep(3)
        self.assert_word(self.get_price_samsung_1(), "68 780 —")
        self.assert_word(self.get_word_samsung_1(), "Планшет Samsung Galaxy Tab S9 FE+ 8/128Gb LTE (Зеленый)")
        self.move_produckt_samsung_1()
        time.sleep(3)
        self.click_to_cart_produckt_samsung_1()
        self.assert_word(self.get_oformlenie_produckta(), "ОФОРМИТЬ")






