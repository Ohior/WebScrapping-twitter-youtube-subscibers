#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-05-28 02:54:04
# @Last Modified by:   Your name
# @Last Modified time: 2022-05-28 16:22:48
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
# with open("data.csv" , 'w', encoding="utf-8") as csv_file:
#     for link in links:
#         csv_file.write(str(link)+"\n")

# with open("data.csv" , 'r', encoding="utf-8") as csv_file:
    # for link in csv_file:
    #     print(link)

with open("data.csv" , 'w', encoding="utf-8") as csv_file:
    for link in links:
        try:
            urls.append(link.attrs["href"])
        except:
            # print(link)n
            csv_file.write(str(link)+"\n")
            continue
print(urls)


   