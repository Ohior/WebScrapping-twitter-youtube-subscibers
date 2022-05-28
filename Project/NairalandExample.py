#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-05-28 02:54:04
# @Last Modified by:   Your name
# @Last Modified time: 2022-05-28 03:18:20
#
#           ____                      ,
#          /---.'.__             ____//
#               '--.\           /.---'
#          _______  \\         //
#        /.------.\  \|      .'/  ______
#       //  ___  \ \ ||/|\  //  _/_----.\__
#      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
#         //   \'. | \'.|.'/ /_/ /  \\
#        //     \ \_\/" ' ~\-'.-'    \\
#       //       '-._| :H: |'-.__     \\
#      //           (/'==='\)'-._\     ||
#      ||                        \\    \|
#      ||                         \\    '
#      |/                          \\
#                                   ||
#                                   ||
#                                   \\
#


from bs4 import BeautifulSoup
import requests

http_address = "https://www.nairaland.com/"
web_address = requests.get(http_address)
page = web_address.content
beautiful_soup = BeautifulSoup(page, "lxml")

links = beautiful_soup.find_all("a")
urls = []
for link in links:
    print(link)
    # for atag in beautiful_soup.find_all("a"):
   