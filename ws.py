import requests
from bs4 import BeautifulSoup
import html5lib
import csv

r = requests.get('http://filipinodoctors.org/cat/dermatology/')

def scrape(r):

    #f = open("scrap.txt", "w+")

    #txt = ''

    with open('doctors.csv', 'w') as f:

        csv_writer = csv.writer(f)
        #head
        csv_writer.writerow(['name', 'address', 'phone'])

        #rows
        soup = BeautifulSoup(r.text, 'html5lib')
        for d in soup.find_all('div', { 'class' : 'description' }):

            for a in d.find_all('a'):
                name = a.text
                r2 = requests.get(a['href'])

                soup2 = BeautifulSoup(r2.text, 'html5lib')

                for d2 in soup2.find_all('div', {'class' : 'item-info'}):
                    a = d2.find('dt', {'class' : 'address'})
                    address = a.find_next_sibling('dd').text

                    p = d2.find('dt', {'class' : 'phone'})

                    if p:
                        phone = p.find_next_sibling('dd').text
                        print(phone)
                    else:
                        pass

                csv_writer.writerow([name, address, phone])

        f.close()

        

    #f.write(txt)
    #f.close()    



if r.status_code == 200:
    scrape(r)        
