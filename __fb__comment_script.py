from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as py

class fbBot:
    def __init__(self,username,password,link,comment,freq):
        self.username=username
        self.password=password
        self.link=link
        self.comment=comment
        self.freq=freq
        self.bot=webdriver.Firefox()


    def login(self):
        bot=self.bot
        bot.get('https://www.facebook.com/')
        time.sleep(3)
        user=bot.find_element_by_id('email')
        user.clear()
        user.send_keys(self.username)
        pas=bot.find_element_by_name('pass')
        pas.clear()
        pas.send_keys(self.password,Keys.ENTER)
        time.sleep(5)
        bot.get(self.link)
        time.sleep(8)
        for i in range(1,self.freq):
            cmnt=bot.find_element_by_link_text('Comment')
            cmnt.click()
            py.write(self.comment)
            py.press('enter')
            time.sleep(2)




username=input("Enter Your Username For Facebook:")
password=input("Enter Your Password For Facebook:")
link=input("Enter The Url Of The Post:")
comment=z=input("Enter Your Comment")
freq=input("Enter Your Frequency For Comments")

z=fbBot(username,password,link,comment,freq)

z.login()