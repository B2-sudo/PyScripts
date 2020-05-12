from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as py

class whatsappBot:
    def __init__(self,victim,msg,num):
        self.victim=victim
        self.msg=msg
        self.num=num
        self.bot=webdriver.Firefox()

    def login(self):
        bot=self.bot
        bot.get('https://web.whatsapp.com/')
        pause=input('Press Anything To Continue!')
        time.sleep(2)

        vic=bot.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        print('hello')
        vic.send_keys(self.victim)
        vic.send_keys(Keys.ENTER)
        time.sleep(2)
        elem=bot.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

        elem.send_keys('Script Time.Chill.And Not Sorry. #B')
        elem.send_keys(Keys.ENTER)

        
        y=self.msg
        for i in range(0,self.num):
            elem.send_keys(y)
            elem.send_keys(Keys.ENTER)
            if(i%100==0):
                print(i)








print('Author-@b\n')

victim=input('Enter The Contact (Exact) : ')
msg=input('Enter Your Message : ')
num=int(input('Enter The Number Of Times You Want To Send: '))
print('Login Now And Enjoy.#B')


plan=whatsappBot(victim,msg,num)

plan.login()


