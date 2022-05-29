#-*- coding: utf-8 -*-
# @Author:  Aigboje Ohiorenua
# @Date:  2022-05-28 16:23:57
# @Last Modified by:   Your name
# @Last Modified time: 2022-05-28 17:23:47


from bs4 import BeautifulSoup

html_doc = """
<html>
    <head><title>Web Scraping Example</title></head>
    <body>
        <p class="title"><b>Web Scraping Example</b></p>
        <p class="story">
            Once upon a time there was a guy who had three names
            <a href="http://example.com/ohis" name="sister" id="link1">Ohis</a>
            <a href="http://example.com/oje" name="sister" id="link2">Oje</a>
            <a href="http://example.com/saint" name="sister" id="link3">Saint</a>
            and he did not know which name to choose
        </p>
        <p class="story">...</p>
        <b class="boldest">Extremely bold</b>
        <blockquote class="boldest">Extremely bold</blockquote>
        <b id='1'>Test 1</b>
        <b another-attribute='1' id='verybold'>Test 2</b>
        <p id="my id"></p>
    </body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html_doc)


soup = BeautifulSoup(html_doc, "lxml")
# print(soup.prettify())
# print(soup.b)
# print(soup.find_all('b')) 
# tag = soup.b
# print(tag)
# change the name of the tag
# tag.name = "blockquote"
# print(tag)
# find the third element
# tag = soup.find_all("b")[2]
# print(tag)
# # get the tag id name
# print(tag["id"])

# extract tag attribute
tag = soup.find_all("b")[3]
# print(tag)
# # get the tag attribute name
# print(tag.attrs)

# alter the attribute value
print(tag)
tag["another-attribute"] = "something"
print(tag.string)
tag.string.replace_with("Diamond girls")
print(tag)
