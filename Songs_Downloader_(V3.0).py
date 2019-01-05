# Importing the required libraries
from bs4 import BeautifulSoup
import webbrowser as web
import requests

url = 'https://pagalworld.co'  # Website URL
source = requests.get(url).text  # Fetching the content
soup = BeautifulSoup(source, 'lxml')  # Parsing the HTML in a soup object

# Fetching the Updates
updates = soup.find('div', class_='onediv')

print('Latest Updates ( Source: www.pagalworld.com )\n')

x = 1                # Serial Counter
first_promot = set()  # Stores First user promots
links1 = []          # Stores webpage links after first promot
final_links2 = []    # Stores links of final webpages filtered in second promot
download_links = []  # Stores Final download links


#============================ Latest Songs List =========================

for content in updates.find_all('li', class_='tnned'):

    # Fetches the link of songs and appends to 'links1' list
    link1 = content.find('a', class_='taga')['href']
    links1.append(link1)

    # Fetches the song name and its details and prints them
    item = content.h3.a.text    # Song name
    details = content.p.text    # Song detail
    print(f'{x}.) {item}  ({details})')  # Display
    x += 1      # Song Serial

#============================= First User Promot =========================

print("=" * 90)
print('\nEnter the serial no. of the item(s) to download (0 to exit) :')

# User Input Promot
for i in range(len(links1)):
    try:
        serial = abs(round(int(input())))

        if serial <= len(links1):  # Checks if user input is appropriate
            if serial == 0:   # Exit condition
                if len(first_promot) == 0:   # Checks if the Input list is empty
                    print('Thank you ! See you next time.')

                break

            # Adds the user input in the first_promot set
            first_promot.add(serial)
        else:
            print("Please Enter the correct Serial No.")
    except:
        print("Please Enter a numerical digit")

#================================ Second Page ==============================

# Iterating over the required Album links
for s in first_promot:
    url_1 = requests.get(links1[s - 1]).text    # Get content
    soup1 = BeautifulSoup(url_1, 'lxml')        # Parsing HTML
    title = soup1.h1.text      # Song / Album Title
    # print(title)

    # Tuple containing details of album items in (name, link) tuple form
    details2 = tuple((sublink.a.h2.text, url + str(sublink.a['href'])) for sublink in soup1.find_all('div', class_='listbox'))

    sec_promot = set()      # Stores Second User promots


#=========================== Second Promot (Optional) ==================

    # If the album contains > 1 songs
    # Display all the songs and take user promot
    if len(details2) > 1:

        print(f'\n{title}:\n')
        for i, detail in enumerate(details2, 1):
            print(f'{i}.) {detail[0]}')

        print('\nEnter serial no. of song of the album to download (0 to exit)')

        # Taking Second User input
        for i in range(len(details2)):
            try:
                promot = abs(round(int(input())))

                # Exit condition
                if promot == 0:
                    break

                elif promot <= len(details2):
                    sec_promot.add(promot)

                else:
                    print('Please enter the correct serial no.')
            except:
                print("Please Enter a numerical digit")

        # Iterating over second input set and storing final required links
        for j in sec_promot:
            final_link2 = details2[j - 1][1]
            final_links2.append(final_link2)

    # IF Single item in an album
    # then directly appending its download link without promot
    elif len(details2) == 1:
        final_links2.append(details2[0][1])  # Fetching and storing link

    # If webpage contains direct download link
    else:
        alt_link = soup1.find('div', class_='downloaddiv').a['href']
        download_links.append(alt_link)

    # Peace :)
    print('\nThank You ! Your downloads shall start soon :)')

#========================== Download Page ==========================

# Iterate over the selected links and fetch their download link
for link in final_links2:
    url_2 = requests.get(str(link)).text   # Get content
    soup2 = BeautifulSoup(url_2, 'lxml')

    d_link = soup2.find('div', class_='downloaddiv').a['href']
    download_links.append(d_link)

#========================= Open Links =========================

# Iterate over the final links and open them in browser
for url in download_links:
    web.open(url)
