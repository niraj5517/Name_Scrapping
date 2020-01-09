from bs4 import BeautifulSoup
import requests
import csv
import os
from bs4 import BeautifulSoup


# print (os.getcwd())
# full_path = os.path.realpath(__file__)
# print(full_path + "\n")

# print("This file directory and name")
# path, filename = os.path.split(full_path)
# print(path + ' --> ' + filename + "\n")

# full_path = os.path.dirname(__file__)
# print(full_path + "\n")

# f=open(full_path+"/abc2.txt","w")
# f.write("honey dates vindicate")


# f.close()

# f=open("./Documents/python/abc2.txt","r")
# print(f.read())

# f.close()
# if os.path.exists("abc2.txt"):
#   print("congrays")
#   print(os.path.abspath('abc2.txt'))
# else:
#   print("The file does not exist")

page = requests.get('https://web.archive.org/web/20121007172912/http://www.nga.gov/collection/anE1.htm')

soup = BeautifulSoup(page.text, 'html.parser')

last_links = soup.find(class_='AlphaNav')
last_links.decompose()

artist_name_list = soup.find(class_='BodyText')

artist_name_list_items = artist_name_list.find_all('a')

full_path = os.path.dirname(__file__)

f= csv.writer(open(full_path+'/nameList.csv','w'))


f.writerow(['Name','Link'])





# print(artist_name_list)
# print("   \n\n\n")
for it in artist_name_list_items:
    
    names=it.contents[0]
    link= 'https://web.archive.org' + it.get('href')

    # print(it.contents[0]+"  "+link)


    
    f.writerow([names,link])


# print(artist_name_list_items)