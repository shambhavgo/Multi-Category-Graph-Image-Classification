import selenium
from selenium import webdriver
import requests
import urllib.request
import datetime
import time
import os 
import keyboard
from bs4 import BeautifulSoup

class meet_bot:
    def __init__(self):
        self.bot = webdriver.Chrome("chromedriver.exe")
    
    def join(self,web_link):
        bot = self.bot
        bot.get(web_link) 
        time.sleep(2)
        gsearch=bot.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div[1]/div[1]/div[1]/div/div[2]/input")        
        gsearch.send_keys(search)
        time.sleep(2)
        serbtn=bot.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div[1]/div[1]/div[1]/button")
        serbtn.click()
        
        #Will keep scrolling down the webpage until it cannot scroll no more
        last_height = bot.execute_script('return document.body.scrollHeight')
        while True:
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            new_height = bot.execute_script('return document.body.scrollHeight')
            try:
                bot.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
                time.sleep(2)
            except:
                pass
            if new_height == last_height:
                break
            last_height = new_height
            
        keyboard.send("Home", do_press=True, do_release=True)
        
        #screenshot
        #parsing
        soup = BeautifulSoup(bot.page_source, 'html.parser')
        #closing web browser
        bot.close()
        #scraping image urls with the help of image tag and class used for images
        img_tags = soup.find_all("img", class_="rg_i")
        count = 0
        for i in img_tags:
            #print(i['src'])
            try:
                #passing image urls one by one and downloading
                urllib.request.urlretrieve(i['src'], str(count)+" "+search+".jpg")
                count+=1
                print("Number of images downloaded = "+str(count),end='\r')
            except Exception as e:
                pass
        
 
     
            
        

link="https://www.google.co.in/imghp?hl=en&authuser=0&ogbl"
search="data table"
obj = meet_bot()
obj.join(link)



