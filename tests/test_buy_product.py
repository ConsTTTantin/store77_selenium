import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from base.base_class import Base
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.planshety_page import PlanshetyPage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test authorization")

    login = MainPage(driver)
    login.authorization()

    print("Finish test authorization")

    print("Start test buy product")

    pl = MainPage(driver)
    pl.link_planshety()

    buy_pl_apple = PlanshetyPage(driver)
    buy_pl_apple.to_cart_planshety_apple()

    driver.refresh()

    time.sleep(2)

    buy_pl_samsung = PlanshetyPage(driver)
    buy_pl_samsung.to_cart_planshety_samsung()

    driver.refresh()

    lcart = PlanshetyPage(driver)
    lcart.click_link_to_cart()
    assert_word = Base(driver)
    assert_word.assert_word(lcart.get_word_cart(), "Оформление заказа")  # Проверяем что находимся в корзине

    avp = CartPage(driver)
    avp.assert_value_planshety()

    time.sleep(5)
    driver.quit()
