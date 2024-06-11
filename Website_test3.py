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
        day_tours = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="featured_exp_nav"]/nav/div[2]')))
        day_tours.click()
        time.sleep(5)
        helicopter = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="feature_experiences_cards"]/div/a[5]')))
        helicopter.click()
        time.sleep(10)

        try:
          popup = WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Judith Blake"]/button/svg'))).click()
        except:
          pass
         
        calendar = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/img')))
        calendar.click()
        time.sleep(5)

        while True:
           random_day = random.randint(1, 31)

           date_xpath = f"//*[@id=\"__next\"]/main/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/div[2]/div/div/div/div[2]/button[{random_day}]"
           try:
              WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="__next"]/main/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/div[2]/div/div/div/div[2]/button[{random_day}]/div')))
              date = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, date_xpath)))
              date.click()
              print(str(random_day) + ': Available')
              break
           except:
              print(str(random_day) + ': Unavailable')
              pass
           
        pax = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"__next\"]/main/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/div[1]/button")))
        pax.click()
        add_adult = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"__next\"]/main/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[3]/button")))
        add_adult.click()
        add_child = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"__next\"]/main/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div[2]/div[3]/button"))) 
        add_child.click()

        book_now = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"__next\"]/main/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/button")))
        book_now.click()
        
        type = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"payment-form\"]/div[1]/input")))
        type.send_keys('Sardar')
        type = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"payment-form\"]/div[2]/input")))
        type.send_keys('Sardar@gmail.com')
        Select = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"payment-form\"]/div[3]/div/div/select/option[166]")))
        Select.click()
        type = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"payment-form\"]/div[3]/div/input")))
        type.send_keys('3124455666')

        iframe = WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#payment-element > div > iframe")))
        Card_Number = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"Field-numberInput\"]")))
        Card_Number.send_keys('4242424242424242')
        Card_Expiry = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"Field-expiryInput\"]")))
        Card_Expiry.send_keys('1225')
        CVC = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"Field-cvcInput\"]")))
        CVC.send_keys('2356')
        Country = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"Field-countryInput\"]/option[160]")))
        Country.click()
        self.driver.switch_to.default_content()
        Pay = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=\"ga4-event-listener-checkout\"]")))
        Pay.click()

        time.sleep(20)
        self.driver.quit()   







website = productChecker()
website.verify_product()