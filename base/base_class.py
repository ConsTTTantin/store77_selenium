import datetime
import re


class Base():

    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")


    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        print(value_word)
        assert value_word == result
        print(f"Good value word {value_word}")


    """Method assert word"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d - %H:%M:%S")
        name_screenshot = f"screenshot {now_date}.png"
        self.driver.save_screenshot("/Users/konstantinsemenkov/PycharmProjects/main_project/screen/" + name_screenshot)


    """Method assert word"""

    def asser_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method price to digit"""

    def price_to_digit(self, price_text):
        digit_price = int(re.sub(r"\D", "", price_text))
        return digit_price

    """Method sum price"""

    def assert_sum_price(self, sum_price, price_1, price_2):
        assert sum_price == price_1 + price_2
        print("GOOD sum price")
