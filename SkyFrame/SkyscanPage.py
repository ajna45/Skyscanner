from SkyFrame.Extensions import Extensions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class SkyscanPage(Extensions):
    """Test data"""
    BASE_URL = "https://rapidapi.com/skyscanner/api/skyscanner-flight-search"
    EMAIL = "ajnahodzic.ah@gmail.com"
    PASS = "Test1234"
    COUNTRY = "BA"
    CURRENCY = "BAM"
    LOCALE = "en-US"
    OUTBOUND_DATE = "anytime"
    INBOUND_DATE = "anytime"
    DESTINATION = "ARN"
    ORIGIN = "SJJ"

    """Web elements"""
    LOGIN_BTN = (By.XPATH, "//*[@id='__next']/section/div[1]/div/div[2]/div/button[1]")
    EMAIL_FLD = (By.ID, "login-form_email")
    PASS_FLD = (By.ID, "login-form_password")
    SIGNIN_BTN = (By.XPATH, "//*[@id='login-form']/div[3]/div/div/div/button")
    PRICING_BTN = (By.XPATH, "//*[@id='__next']/section/main/div/div[1]/section/div[2]/div/div/div/div[1]/div/a[4]")
    SELECT_PLAN_BTN = (By.XPATH, "//*[@data-hook='pricing-table-subscribe-btn']/span")
    ACCOUNT =(By.XPATH, "//*[@id='__next']/section/main/div/div[2]/div/div/div/div/div[2]/div[1]/div")
    ENDPOINTS_BTN = (By.XPATH, "//*[@id='__next']/section/main/div/div[1]/section/div[2]/div/div/div/div[1]/div/div/a")
    PLACES_BTN = (By.XPATH, "//*[@id='collapse_panel_5a9b5affe4b00687d357312c']/div[1]")
    BROWSE_PRICES_BTN = (By.XPATH, "//*[@id='collapse_panel_5aa1ea8de4b00687d3574278']/div")
    LOCALISATION_BTN = (By.XPATH, "//*[@id='collapse_panel_5b073fb1e4b09d99505e1e3d']/div")
    GET_CURRENCIES_BTN = (By.XPATH, "//*[@id='collapse_panel_5b073fb1e4b09d99505e1e3d']/div[2]/div/div[2]/div/span[2]")
    GET_BROWSE_DATES = (By.XPATH, "//div[@title='Browse Dates']")
    TEST_ENDPOINT_BTN = (By.XPATH, "//span[@translationkey='test_endpoint']")
    CODE_MSG = (By.XPATH, "//div[@class='content']/div/span[1]")
    BTN = (By.XPATH, "//*[@id='__next']/section/main/div/div[1]/section/div[2]/div/div/div/div[2]/div/div[1]/button/span")
    COUNTRY_FLD =(By.XPATH, "//*[@id='endpoint-form_5aa1edd6e4b0a62b51d070ac']")
    CURRENCY_FLD = (By.XPATH, "//*[@id='endpoint-form_5aa1edd6e4b0a62b51d070ad']")
    LOCALE_FLD = (By.XPATH, "//*[@id='endpoint-form_5aa1edd7e4b04378c0c9a78f']")
    OUTBOUND_DATE_FLD =(By.XPATH, "//*[@id='endpoint-form_5aa1edd8e4b04378c0c9a790']")
    INBOUND_DATE_FLD = (By.XPATH, "//*[@id='endpoint-form_5c193622e4b067d7d9562ce7']")
    DESTINATION_FLD = (By.XPATH, "//*[@id='endpoint-form_5aa1edd7e4b084deb4ea6ef6']")
    ORIGIN_FLD = (By.XPATH, "//*[@id='endpoint-form_5aa1edd7e4b0a62b51d070ae']")

    """Constructor of Skyscanner page"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.BASE_URL)

    """Login method"""
    def login(self):
        time.sleep(5)
        self.is_visible(self.LOGIN_BTN)
        self.do_click(self.LOGIN_BTN)
        time.sleep(1)
        self.do_send_keys(self.EMAIL_FLD, self.EMAIL)
        self.do_send_keys(self.PASS_FLD, self.PASS)
        self.do_click(self.SIGNIN_BTN)

    """Subscribe to the Skyscanner API method"""
    def subscribe(self):
        time.sleep(3)
        self.do_click(self.PRICING_BTN)
        time.sleep(1)
        if self.is_visible(self.ACCOUNT) == True:
            self.do_click(self.BTN)
        else:
            self.do_click(self.SELECT_PLAN_BTN)
            self.do_click(self.BTN)

    """Test Endpoint of Get Currencies"""
    def get_currencies(self):
        time.sleep(3)
        self.do_click(self.LOCALISATION_BTN)
        time.sleep(1)
        self.do_click(self.GET_CURRENCIES_BTN)
        time.sleep(1)
        self.do_click(self.TEST_ENDPOINT_BTN)
        time.sleep(1)
        flag = True
        if self.get_element_text(self.CODE_MSG) != "200":
            flag = False
        return flag

    """Test endpoint of Browse Dates"""
    def get_browse_dates(self):
        self.do_click(self.BROWSE_PRICES_BTN)
        time.sleep(1)
        self.do_click(self.GET_BROWSE_DATES)
        time.sleep(1)
        self.do_clear(self.COUNTRY_FLD)
        self.do_send_keys(self.COUNTRY_FLD, self.COUNTRY)
        self.do_clear(self.CURRENCY_FLD)
        self.do_send_keys(self.CURRENCY_FLD, self.CURRENCY)
        self.do_clear(self.LOCALE_FLD)
        self.do_send_keys(self.LOCALE_FLD, self.LOCALE)
        self.do_clear(self.ORIGIN_FLD)
        self.do_send_keys(self.ORIGIN_FLD, self.ORIGIN)
        self.do_clear(self.DESTINATION_FLD)
        self.do_send_keys(self.DESTINATION_FLD, self.DESTINATION)
        self.do_clear(self.OUTBOUND_DATE_FLD)
        self.do_send_keys(self.OUTBOUND_DATE_FLD, self.OUTBOUND_DATE)
        self.do_clear(self.INBOUND_DATE_FLD)
        self.do_send_keys(self.INBOUND_DATE_FLD, self.INBOUND_DATE)
        time.sleep(1)
        self.scroll_to_beginning()
        self.do_click(self.TEST_ENDPOINT_BTN)
        time.sleep(1)
        flag = True
        if self.get_element_text(self.CODE_MSG) != "200":
            flag = False
        return flag