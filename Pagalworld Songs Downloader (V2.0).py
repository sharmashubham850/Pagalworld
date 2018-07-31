from bs4 import BeautifulSoup
import webbrowser as web
import requests

url = 'https://pagalworld.co'
source = requests.get(url).text
soup  = BeautifulSoup(source , 'lxml')

updates = soup.find( 'div' , class_ = 'onediv')
#print(updates)

print('Latest Updates ( Source: www.pagalworld.com )\n')
x = 1
serials = []
links1 = []
links2 = []
final_links2 = []
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
            pass
        else:
            print('Thank you ! See you next time.')
        break
    serials.append(serial)

        
for s in serials:
    url_1 = requests.get(links1[s-1]).text
    soup1 = BeautifulSoup( url_1 , 'lxml')
    #print(soup1.prettify())
    title = soup1.h1.text
    #print(title)

    links2 = []
    promots = []
    names = []
    
    for sublink in soup1.find_all( 'div' , class_ = 'listbox'):
        link2 = url + str(sublink.a['href'])
        name = sublink.a.h2.text
        #print(link2)
        links2.append(link2)
        names.append(name)
        
    if len(links2) > 1:
        print(f'\n{title}:\n')
        #print(links2)
        for name in names:
            print(name)

        print('\nEnter the serial no. of song of the album to download (0 to exit)')
        
        for i in range(len(links2)):
            promot = int(input())
            if promot == 0:
                break
            promots.append(promot)
        
        for j in promots:
            final_link2 = links2[j-1]
            final_links2.append(final_link2)
            
    elif len(links2) == 1:
        final_links2.append(links2[0])

    else:
        alt_link = soup1.find( 'div' , class_ = 'downloaddiv').a['href']
        download_links.append(alt_link)

#print(final_links2)

print('\nThank You ! Your downloads shall start soon :)')
            
for link in final_links2:
    url_2 = requests.get(str(link)).text
    soup2 = BeautifulSoup( url_2 , 'lxml')
    #print(soup2.prettify())

    download_link = soup2.find( 'div' , class_ = 'downloaddiv').a['href']
    #print(download_link)

    download_links.append(download_link)

#print(download_links)

for url in download_links:
    web.open(url)
