from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

"""This is the main class of the Skyscanner API"""
"""It contains all the generic methods """

class Extensions:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        self.do_clear(by_locator)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def scroll_to_beginning(self ):
        self.driver.execute_script("window.scrollTo(0,0);")

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def do_clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.CONTROL + "a")
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.CLEAR)

