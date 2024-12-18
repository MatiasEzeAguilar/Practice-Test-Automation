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
    
def test_check_title(setup_and_teardown):
    
    driver = setup_and_teardown

    title = driver.get_title()
    assert "The Internet" in title, f"Expected 'The Internet' in title, but got {title}"

def test_check_input_username(setup_and_teardown):

    driver = setup_and_teardown

    username = driver.get_username()
    username.send_keys("tomsmith")

def test_check_input_password(setup_and_teardown):
    
    driver = setup_and_teardown

    password = driver.get_password()
    password.send_keys("SuperSecretPassword!")

def test_login(setup_and_teardown):

    driver = setup_and_teardown

    login = driver.get_login()
    login.click()

def test_check_flash_messages_into(setup_and_teardown):
    
    driver = setup_and_teardown

    flash_message = driver.get_flash_messages()

    assert "You logged into a secure area!" in flash_message

def test_close_flash_messages(setup_and_teardown):

    driver = setup_and_teardown

    close = driver.close_flash_messages()
    close.click()

def test_check_logout(setup_and_teardown):

    driver = setup_and_teardown

    logout = driver.get_logout()
    logout.click()

def test_check_flash_messages_out(setup_and_teardown):
    
    driver = setup_and_teardown

    flash_message = driver.get_flash_messages()

    assert "You logged out of the secure area!" in flash_message

    time.sleep(2)