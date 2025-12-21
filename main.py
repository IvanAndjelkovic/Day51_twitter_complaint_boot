import os
from dotenv import load_dotenv
from selenium import webdriver



load_dotenv()

twitter_mail=os.getenv("TWITTER_EMAIL")
twitter_pass=os.getenv("TWITTER_PASSWORD")





PROMISED_DOWN=150
PROMISED_UP=10
# CHROME_DRIVER_PATH="/usr/local/bin/chromedriver"
twitter_mail=os.getenv("TWITTER_EMAIL")
twitter_pass=os.getenv("TWITTER_PASSWORD")





class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0 

    def get_internet_speed(self):
        print("vrlo dobro")
    def tweet_at_provider(self):
        print("mile")



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()