from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

import time

class Scraper:
    
    def __init__(self, email: str, password: str):
        self.driver = webdriver.Chrome()
        self.email = email
        self.password = password
    
    def start(self, profiles: list[str]):
        self.driver.get(profiles[0]) #Trying to get to first profile
        
        self.driver.implicitly_wait(10)
        
        urls = [{}]
        
        #If we encounter Agree and join page 
        if self.driver.find_element(By.ID, "email-or-phone") and self.driver.find_element(By.ID, "password"):
            self.login_form()
                    
            for profile in profiles:
                try:
                    self.driver.get(profile + "/overlay/contact-info/")
                    email_elements = self.driver.find_element(By.XPATH,'//a[starts-with(@href, "mailto:")]')
                    
                    self.driver.implicitly_wait(10)
                    
                    print(email_elements)
                    
                    emails = [email_element.get_attribute("href") for email_element in email_elements]
                    emails = set(emails)
                    emails = [str(email).replace("mailto:","") for email in emails]
                    print(emails)
            
                except Exception as e:
                    print(e)
                    continue
                    
        
        else:
            pass
            
    
    def login_form(self):
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "authwall-join-form__form-toggle--bottom").click()
        self.driver.implicitly_wait(10)
        
        email_input = self.driver.find_element(By.ID, "session_key")
        
        password = self.driver.find_element(By.ID, "session_password")
        class_name = "btn-md btn-primary flex-shrink-0 cursor-pointer sign-in-form__submit-btn--full-width w-full max-w-[400px] mx-auto"
        print("chomu")
       
        email_input.send_keys(self.email)
        time.sleep(5)
        password.send_keys(self.password)
        time.sleep(2)

        password.send_keys(Keys.ENTER)
        return

scraper = Scraper("ENTER EMAIL HERE", "ENTER PASSWORD HERE")
scraper.start(["https://www.linkedin.com/in/chahat-sagar-aaab67222/"])
