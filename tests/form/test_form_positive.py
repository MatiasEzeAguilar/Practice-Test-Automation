import pytest
from web_driver import WebDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture(scope="module")
def setup_and_teardown():
    
    driver = WebDriverManager()
    driver.setup_driver()
    
    yield driver
    driver.close_driver()

def test_open_thePlayground(setup_and_teardown):
    
    driver = setup_and_teardown
    driver.open_url("https://play1.automationcamp.ir/forms.html")
    
def test_check_title(setup_and_teardown):
    
    driver = setup_and_teardown

    title = driver.get_title()
    assert "Form Interactions" in title, f"Expected 'Form Interactions' in title, but got {title}"

def test_check_exp_placeholder(setup_and_teardown):

    driver = setup_and_teardown

    placeholder = driver.get_exp_input().get_attribute("placeholder")

    assert 'years of automation experience' in placeholder

def test_check_exp_input(setup_and_teardown):

    driver = setup_and_teardown

    exp = driver.get_exp_input()
    exp.send_keys("1")

    time.sleep(2)

def test_checkbox(setup_and_teardown):

    driver = setup_and_teardown
    
    check_python = driver.get_check_python()
    check_python.click()

    time.sleep(1)

    check_javaScript = driver.get_check_javaScript()
    check_javaScript.click()
    
    time.sleep(2)

def test_radio(setup_and_teardown):

    driver = setup_and_teardown

    rad_protractor = driver.get_radio_protractor()
    rad_protractor.click()

    time.sleep(1)

    rad_selenium = driver.get_radio_selenium()
    rad_selenium.click()
    
    time.sleep(2)

def test_select_skill(setup_and_teardown):

    driver = setup_and_teardown

    select_element = driver.get_select_skill()
    select = Select(select_element)
    select.select_by_value("cyp")

    time.sleep(1)

    select.select_by_value("pro")

    time.sleep(1)

    select.select_by_value("sel")

    time.sleep(2)

def test_select_lenguage(setup_and_teardown):

    driver = setup_and_teardown

    select_element = driver.get_select_lenguage()
    select = Select(select_element)
    select.select_by_value("java")

    time.sleep(1)

    select.deselect_by_value("java")
    select.select_by_value("typescript")

    time.sleep(1)

    select.deselect_by_value("typescript")
    select.select_by_value("javascript")

    time.sleep(1)

    select.deselect_by_value("javascript")
    select.select_by_value("python")

    time.sleep(2)

def test_texarea(setup_and_teardown):

    driver = setup_and_teardown

    placeholder = driver.get_textarea().get_attribute("placeholder")

    assert 'Notes' in placeholder

    notes = driver.get_textarea()
    notes.send_keys("This is a space for notes.")

    time.sleep(1)

    notes.clear()
    notes.send_keys("Este es un espacio para notas.")

    time.sleep(2)

def test_speaks_german(setup_and_teardown):

    driver = setup_and_teardown

    check_german = driver.get_check_german()
    check_german.click()

    time.sleep(1)

    check_german.click()

    time.sleep(2)

#def test_fluency(setup_and_teardown):

#    driver = setup_and_teardown

#    fluency = driver.get_input_range()

#    actions = ActionChains(driver)
#    actions.click_and_hold(fluency).move_by_offset(5, 0).release().perform()

#    time.sleep(1)

#    actions.click_and_hold(fluency).move_by_offset(-5, 0).release().perform()

#    time.sleep(2)

def test_form_validations(setup_and_teardown):

    driver = setup_and_teardown
    driver.scroll_down()

    time.sleep(1)

    city = driver.get_input_city()
    city.send_keys("Rosario")

    time.sleep(1)

    state = driver.get_input_state()
    state.send_keys("Argentina")

    time.sleep(1)

    zip = driver.get_input_zip()
    zip.send_keys("2000")

    time.sleep(2)

def test_check_form_validations(setup_and_teardown):

    driver = setup_and_teardown

    validations = driver.get_checkbox_invalid()
    validations.click()

    time.sleep(2)

def test_button_form(setup_and_teardown):

    driver = setup_and_teardown

    submit = driver.get_button_form()
    submit.click()

    time.sleep(2)