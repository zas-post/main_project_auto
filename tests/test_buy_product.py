import time
import allure
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

@allure.description("Test buy product")
def test_buy_product(set_group):
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches',[ 'enable-logging' ])
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

    print("---- Start Test ----")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()
    print("---- Finish Test ----")

    driver.quit()
