import pytest
from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    web_driver.maximize_window()
    yield
    web_driver.close()
