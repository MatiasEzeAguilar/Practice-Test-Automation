from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con

class WebDriverManager:
    def __init__(self):

        self.driver = None
    
    def setup_driver(self):
        
        service = Service(EdgeChromiumDriverManager().install())
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()
    
    def open_url(self, url):
        
        if self.driver is None:
            self.setup_driver()
        self.driver.get(url)
    
    def close_driver(self):
        
        if self.driver:
            self.driver.quit()
            self.driver = None
    
    def get_title(self):

        if self.driver:
            return self.driver.title
        return None
    
    def scroll_down(self):

        self.driver.execute_script("window.scrollBy(0, 700);")

#Test Login
    
    def get_username(self):
        
        return self.driver.find_element(By.ID, "username")

    def get_password(self):

        return self.driver.find_element(By.ID, "password")
    
    def get_login(self):

        return self.driver.find_element(By.CLASS_NAME, "radius")
    
    def get_flash_messages(self):

        return self.driver.find_element(By.ID, "flash").text
    
    def close_flash_messages(self):

        return self.driver.find_element(By.CLASS_NAME, "close")
    
    def get_logout(self):
        
        logout_button = WebDriverWait(self.driver, 10).until(
            exp_con.element_to_be_clickable((By.CLASS_NAME, "button.secondary.radius"))
        )
        return logout_button

#Test Form

    def get_exp_input(self):

        exp_input = WebDriverWait(self.driver, 10).until(
            exp_con.visibility_of_element_located((By.ID, "exp"))
        )
        return exp_input
    
    def get_check_python(self):

        return self.driver.find_element(By.ID, "check_python")
    
    def get_check_javaScript(self):

        return self.driver.find_element(By.ID, "check_javascript")
    
    def get_radio_selenium(self):

        return self.driver.find_element(By.ID, "rad_selenium")
    
    def get_radio_protractor(self):

        return self.driver.find_element(By.ID, "rad_protractor")
    
    def get_select_skill(self):

        return self.driver.find_element(By.ID, "select_tool")
    
    def get_select_lenguage(self):

        return self.driver.find_element(By.ID, "select_lang")
    
    def get_textarea(self):

        return self.driver.find_element(By.ID, "notes")
    
    def get_check_german(self):

        return self.driver.find_element(By.CSS_SELECTOR, "label[for='german']")
    
    def get_input_range(self):

        return self.driver.find_element(By.ID, "fluency")
    
    def get_input_city(self):

        return self.driver.find_element(By.ID, "validationCustom03")
    
    def get_input_state(self):

        return self.driver.find_element(By.ID, "validationCustom04")
    
    def get_input_zip(self):

        return self.driver.find_element(By.ID, "validationCustom05")
    
    def get_checkbox_invalid(self):

        return self.driver.find_element(By.ID, "invalidCheck")
    
    def get_button_form(self):

        submit_button = WebDriverWait(self.driver, 10).until(
            exp_con.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/form/button"))
        )
        return submit_button