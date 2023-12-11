# import time
# import allure
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from pages.main_page import MainPage
#
#
# def test_authorization():
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     g = Service()
#     driver = webdriver.Chrome(options=options, service=g)
#
#     print("Start test authorization")
#
#     login = MainPage(driver)
#     login.authorization()
#
#     print("Finish test authorization")
#     time.sleep(2)
#     driver.quit()
