from bs4 import BeautifulSoup
import webbrowser as web
import requests

pagalworld = 'https://pagalworld.co'
source = requests.get(pagalworld).text
soup  = BeautifulSoup(source , 'lxml')

updates = soup.find( 'div' , class_ = 'onediv')
#print(updates)

print('Pagalworld Latest Updates:\n')
x = 1
n = 0
serials = []
links1 = []
download_links = []

for content in updates.find_all('li' , class_ = 'tnned'):
    item = content.h3.a.text
    details = content.p.text
    print(f'{x}.) {item}  ({details})')
    x+=1
    
for content in updates.find_all('li' , class_ = 'tnned'):
    link1 = content.find( 'a' , class_ = 'taga')['href']
    links1.append(link1)
    
#print(links1)

print('\nEnter the serial no. of the item(s) you want to download ( 0 to exit ) :')

for i in range(len(links1)):
    serial = int(input())
    if serial == 0:
        if len(serials)>0:
            print('Thank you ! Your downloads shall start soon :)')
        else:
            print('Thank you ! See you next time.')
        break
    serials.append(serial)
    
for s in serials:
    source1 = requests.get(links1[s-1]).text
    soup1 = BeautifulSoup( source1 , 'lxml')
    #print(soup1.prettify())
    title = soup1.h1.text
    #print(title)
    
    sublink = soup1.find( 'div' , class_ = 'listbox')
    link2 = pagalworld + str(sublink.a['href'])
    #print(link2)
        
    
        
        

    source2 = requests.get(str(link2)).text
    soup2 = BeautifulSoup( source2 , 'lxml')
    #print(soup2.prettify())

    download_link = soup2.find( 'div' , class_ = 'downloaddiv').a['href']
    #print(download_link)

    download_links.append(download_link)

#print(download_links)

for url in download_links:
    web.open(url)
