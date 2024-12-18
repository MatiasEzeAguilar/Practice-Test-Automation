import pytest
from web_driver import WebDriverManager
import time

@pytest.fixture(scope="module")
def setup_and_teardown():
    
    driver = WebDriverManager()
    driver.setup_driver()
    
    yield driver
    driver.close_driver()

def test_open_theInternet(setup_and_teardown):
    
    driver = setup_and_teardown
    driver.open_url("https://the-internet.herokuapp.com/login")

def test_check_input_username_failed(setup_and_teardown):

    driver = setup_and_teardown

    username = driver.get_username()
    username.send_keys("testuser")

def test_check_input_password_falied(setup_and_teardown):
    
    driver = setup_and_teardown

    password = driver.get_password()
    password.send_keys("testpassword")

def test_login_falied(setup_and_teardown):

    driver = setup_and_teardown

    login = driver.get_login()
    login.click()

def test_check_flash_messages_error(setup_and_teardown):
    
    driver = setup_and_teardown

    flash_message = driver.get_flash_messages()

    assert "Your username is invalid!" in flash_message

def test_close_flash_messages_error(setup_and_teardown):

    driver = setup_and_teardown

    close = driver.close_flash_messages()
    close.click()

    time.sleep(2)