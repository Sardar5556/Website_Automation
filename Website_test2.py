import time
import random
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class productChecker:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)

    def verify_product(self):
        self.driver.get("https://www.tripshepherd.com")
        time.sleep(5)

        small_group = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="experience"]/div[1]/a/div/div/img')))
        small_group.click()
        time.sleep(5)

        self.driver.back()
        time.sleep(5)

        free_cancellation = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="experience"]/div[2]/a/div/div/img')))
        free_cancellation.click()
        time.sleep(2)
        
        FAQ_1 = WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,'//*[@id="faq"]/div/div/img[1]')))
        for i in range(0,6):
            FAQ_1[i].click()
            time.sleep(5)
            FAQ_1[i].click()
            time.sleep(2)


        self.driver.back()
        time.sleep(15)

        star = WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="experience"]/div[3]/a/div/div/img')))
        star.click()
        time.sleep(15)
        


website = productChecker()
website.verify_product()


   