#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-05-28 17:26:15
# @Last Modified by:   Your name
# @Last Modified time: 2022-05-29 10:13:26

from bs4 import BeautifulSoup
import requests



def getWebAddress(address=''):
    if(address):
        url = input("Enter url link: ")
    else:
        url = address
    address = requests.get(url)
    return address

def getWebPage(address):
    page = address.content
    soup = BeautifulSoup(page, "lxml")
    return soup

def prettifyWebPage(page):
    prettify = page.prettify()
    return prettify

def downloadFile(downloadlink='', filename=''):
    with getWebAddress(address=downloadlink) as req:
        try:
            if(filename):# if file has a name
                pass
            else:# file does not have a name
                filename = req.url[downloadlink.rfind('/')+1:]
            with open(filename, "wb") as f:
                for data in req.iter_content():
                    if(data):
                        f.write(data)
            return filename
        except Exception as e:
            print(e)
            return None
