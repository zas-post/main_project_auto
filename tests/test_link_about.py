import time

import allure
from selenium import webdriver

from pages.login_page import Login_page
from pages.main_page import Main_page


@allure.description("Test link about")
def test_link_about():
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches',[ 'enable-logging' ])
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

    print("--- Start Test ---")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("---- Finish Test ----")
    # enter_shopping_cart = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
    # enter_shopping_cart.click()
    # print(f"- Click Enter Shopping Cart")

    # success_test = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
    # value_success_test = success_test.text
    # print(value_success_test)
    # assert value_success_test == "YOUR CART"
    # print("Test Success!!! ---> Your Cart")
    driver.quit()

# WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='visibleAfter']")))

# test = Test_1()
# test.test_select_product()

# time.sleep(5)
# driver.close()
