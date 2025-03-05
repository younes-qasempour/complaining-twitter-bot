import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


load_dotenv()


class InternetSpeedTwitterBot:

    def __init__(self):

        self.driver = webdriver.Chrome()
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
        self.down = down_speed.text
        self.up = up_speed.text



    def tweet_at_provider(self):
        self.driver.get("https://x.com/home")

        time.sleep(5)
        user_name_input = self.driver.find_element(By.NAME, "text")
        user_name_input.send_keys(os.getenv("X_EMAIL"))
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]"
                                           "/div/div/div[2]/div[2]/div/div/div/button[2]").click()

        time.sleep(2)
        phone_input = self.driver.find_element(By.NAME, "text")
        phone_input.send_keys(os.getenv("X_PHONE"))
        phone_input.send_keys(Keys.ENTER)

        time.sleep(2)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(os.getenv("X_PASSWORD"))
        password_input.send_keys(Keys.ENTER)

        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/"
                                           "button[2]").click()

        time.sleep(3)
        tweet = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay "
                 f"for {os.getenv("PROMISED_DOWN")}down/{os.getenv("PROMISED_UP")}up?")
        x_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/"
                                                     "div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/"
                                                     "div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]"
                                                     "/div/div/div/div")
        x_input.send_keys(tweet)

        time.sleep(3)
        post_button = self.driver.find_element(By.CSS_SELECTOR,'[data-testid="tweetButtonInline" ')
        post_button.click()

        self.driver.quit()



bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()