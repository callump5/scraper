from bs4 import BeautifulSoup
import googlespider
import requests
import re
import csv


urls = [
    'https://www.segrave.co.uk',
    'https://www.buckleywatson.co.uk',
    'https://www.goldingaccountancy.co.uk',
    'https://clouders.co.uk',
    'www.plattrushton.co.uk',
    'https://www.francisjamesllp.co.uk',
    'www.cksonline.co.uk',
    'merryfield-accountants.com',
    'www.slm.tax',
    'https://mcl.accountants',
    'https://tblaccountants.co.uk',
    'www.nuttgens.uk.com',
    'https://threebestrated.co.uk/accountants-in-southend-on-sea',
    'www.eh-taylors.co.uk',
    'https://aphaccountancy.co.uk',
    'https://www.devinesaccountants.co.uk',
]

companies = []
numbers = []

i = 0
for url in urls:
    try:
        print(url)
        r = requests.get(url)

        html = BeautifulSoup(r.text, 'html.parser')
        tel = re.findall('(01702\s[0-9]{6})|(01702[0-9]{6})|(01702\s[0-9]{3}\s[0-9]{3})', str(r.text))
        title = re.findall('title', str(r.text))
        title_text = html.title.text


        if len(tel[0][0]) > 5:
            comp_tel = tel[0][0]
        elif len(tel[0][1]) > 5:
            comp_tel = tel[0][1]
        elif len(tel[0][2]) > 5:
            comp_tel = tel[0][2]

        number = str(comp_tel)
        company =  {'company': title_text}
        company_number = {'number': number}
        companies.append(company)
        numbers.append(number)
    except:
        print('something fucked up')


length = len(companies)
ind = 0

f = open('companies.csv', 'w')
writer = csv.writer(f)

while ind < length:
    writer.writerow((companies[ind]['company'], numbers[ind]))
    ind += 1


f.close()
ind = 0