import datetime



class Base():
    def __init__(self, driver):
        self.driver = driver

    """ Method get current URL """

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Curent URL {get_url}")

    """ Method assert word """

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """ Method Screenshot """

    def get_screenshot(self):
        new_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot1_{new_date}.png'
        # driver.save_screenshot(name_screenshot)
        # driver.save_screenshot('C:\\drive_d\\GIT\\python_selenium_s\\srceen\\' + name_screenshot )
        self.driver.save_screenshot('.\\screen\\' + name_screenshot)
        print(f'screenshot_{new_date}.png')

    """ Method assert URL """

    def aseert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")
