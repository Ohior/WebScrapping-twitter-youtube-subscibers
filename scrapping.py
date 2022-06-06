#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-05-30 12:57:47
# 
#    /\`.   ,'/\
#   //\\0 " 0//\\       @Last Modified by:   Your name
#  //    ,^.    \\      @Last Modified time: 2022-06-06 20:23:22
#  \\           //
#   \\         //
#

from datetime import datetime
import sqlite3
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def saveData(twitter, youtube):
    data = {
        'twitter':twitter,
        'youtube':youtube,
        'data':datetime.now().strftime('%d, %m, %y')
    }
    con = sqlite3.connect('followers.db')
    cur = con.cursor()
    
    # create table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS follow_stats (
            data TEXT, youtube TEXT, twitter TEXT
        )
    ''')
    insert  = cur.execute(
        'INSERT INTO follow_stats VALUES ("{}","{}","{}")'.format(data['data'], data['youtube'], data['twitter'])
    )
    # commit to database
    con.commit()
    con.close()

# use chrome
option = webdriver.ChromeOptions()
# stop browser from displaying
option.add_argument('headless')
# setup driver
# driver = webdriver.Chrome(executable_path='./chromedriver', options=option)
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service, options=option)
# amount of time to wait when looking for something on webpage
driver.implicitly_wait(15)
# prevent selenium from opening browser
# YOUTUBE
driver.get('https://www.youtube.com/watch?v=b80a8XKX6ws')
# youtube_data = driver.find_element_by_id("owner-sub-count").text
youtube_data = driver.find_element(by=By.ID, value="owner-sub-count").text
# TWITTER
driver.get('https://twitter.com/OhiorOje')
# element_data = int(driver.find_element_by_css_selector('a[href="/OhiorOje/followers"] > span').text)
twitter_data = driver.find_element(By.CSS_SELECTOR, 'a[href="/OhiorOje/followers"] > span').text

driver.quit()

saveData(twitter_data, youtube_data)
