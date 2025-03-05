import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


load_dotenv()


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(self.chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        reject_button = self.driver.find_element(By.ID, "onetrust-reject-all-handler")
        reject_button.click()
        time.sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()
        time.sleep(120)
        down_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        up_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.down = int(down_speed.text)
        self.up = int(up_speed.text)


    def tweet_at_provider(self):
        pass



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()