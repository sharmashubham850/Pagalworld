from bs4 import BeautifulSoup
import webbrowser as web
import requests
import datetime
import csv

today = datetime.date.today()

csv_file = open(rf'C:\Users\sharm\Desktop\Pagalworld Latest Updates ({today}).csv' , 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Sr. No.' , 'Update' , 'Download Link'])

url = 'https://pagalworld.co'
source = requests.get(pagalworld).text
soup  = BeautifulSoup(source , 'lxml')

top_content = soup.find( 'div' , class_ = 'onediv')
#print(updates)

print('Pagalworld Latest Updates:\n')
x = 1

for content in top_content.find_all('li' , class_ = 'tnned'):
    item = content.h3.a.text
    details = content.p.text
    print(f'{x} - {item}  ({details})')

    link = content.find( 'a' , class_ = 'taga')['href']
    #print(link)

    source1 = requests.get(str(link)).text
    soup1 = BeautifulSoup( source1 , 'lxml')
    #print(soup1.prettify())

    link1 = soup1.find( 'div' , class_ = 'listbox').a['href']
    link1 = pagalworld + str(link1)
    #print(link1)

    source2 = requests.get(str(link1)).text
    soup2 = BeautifulSoup( source2 , 'lxml')
    #print(soup2.prettify())

    download_link = soup2.find( 'div' , class_ = 'downloaddiv').a['href']
    #print(download_link)

    #web.open(download_link)

    csv_writer.writerow([x , f'{item} ({details})' , download_link])

    x+=1

csv_file.close()







