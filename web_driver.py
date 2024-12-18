from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_con

class WebDriverManager:
    def __init__(self):

        self.driver = None
    
    def setup_driver(self):
        
        self.driver = webdriver.Edge()
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