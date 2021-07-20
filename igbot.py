from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:\Users\rodri\Desktop\python\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")

BobBot = instagramBot('jorgenoites12','otario123')
BobBot.login()