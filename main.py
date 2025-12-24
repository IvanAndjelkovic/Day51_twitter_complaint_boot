import os
from dotenv import load_dotenv
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




load_dotenv()

twitter_mail=os.getenv("TWITTER_EMAIL")
twitter_pass=os.getenv("TWITTER_PASSWORD")

speed_test_url="https://www.speedtest.net/"

go_button_xpath='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]'
accept_privacy_button_xpath = '//*[@id="onetrust-accept-btn-handler"]'
download_speed_xpath = '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
upload_speed_xpath ='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'



PROMISED_DOWN=150
PROMISED_UP=10
# CHROME_DRIVER_PATH="/usr/local/bin/chromedriver"
twitter_mail=os.getenv("TWITTER_EMAIL")
twitter_pass=os.getenv("TWITTER_PASSWORD")

# Keep  Chrome browser open after  program finishes







class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",  True)
        self.driver = webdriver.Chrome()



        self.down = 0
        self.up = 0 

    def get_internet_speed(self):
        self.driver.get(speed_test_url)
        wait  = WebDriverWait(self.driver,2)
        accept_privacy_button=wait.until(EC.element_to_be_clickable((By.XPATH ,accept_privacy_button_xpath)))
        accept_privacy_button.click()
        wait  = WebDriverWait(self.driver,2)
        go_button=wait.until(EC.element_to_be_clickable((By.XPATH ,go_button_xpath)))
        go_button.click() 

        wait  = WebDriverWait(self.driver,2)
        time.sleep(60)
        download_speed= wait.until(EC.element_to_be_clickable((By.XPATH ,download_speed_xpath ))) 
        download_speed_text = download_speed.text
        upload_speed= wait.until(EC.element_to_be_clickable((By.XPATH ,upload_speed_xpath ))) 
        upload_speed_text = upload_speed.text
        print(download_speed_text, upload_speed_text)
        






    def tweet_at_provider(self):
        print("mile")



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
time.sleep(20)
