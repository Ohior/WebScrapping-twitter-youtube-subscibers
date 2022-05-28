import io
import  requests
# requests help us access website
from bs4 import BeautifulSoup
# this will help us scrap the website



web_address = "https://www.google.com/"

result = requests.get(web_address)
# check id the site is accessible. 200 mean yes
print(result.status_code)
# print(result.headers)

# store the page info
src = result.content
# print(src)

# now to proccess  the src data
soup = BeautifulSoup(src, "lxml")
# soup = BeautifulSoup(src, "html.parser")
# soup = BeautifulSoup(src, "html5lib")
links = soup.find_all("a")
# with io.open("fname.txt", "w", encoding="utf-8") as f:
#     for i in links:
#         f.writelines(str(i)+"\n")
# print(links)
# print("\n")
# check if a link has a keyword and get the link
for link in links:
    if("About" in link.text):
        print(link)
        print(link.attrs['href'])

