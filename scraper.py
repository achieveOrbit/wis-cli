#!/bin/python
import requests
import re
from bs4 import BeautifulSoup

class Termin:

        def __init__(self, date, subject, term_type, name):
                self.date      = date
                self.subject   = subject
                self.term_type = term_type
                self.name      = name

        def formatter(self):
                print("Date      | Subject | Type | Name              ")
                print("%10s|%9s|%6s|%20s" % (self.date, self.subject, self.term_type, self.name))


page = requests.get("https://wis.fit.vutbr.cz/FIT/st/news-c.php", verify=False, auth=('xlogin00', 'password'))
soup = BeautifulSoup(page.content, "html.parser")
tr = soup.find_all(attrs={"bgcolor":"#dfe7cf"}) + soup.find_all(attrs={"bgcolor":"#FFF8DC"})

#print(tr)

print("=======================")

for item in tr:
    #datum
    print(re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", str(item)))
    #predmet
    print(str(re.findall(r"<b>[A-Z0-9]{3}</b>", str(item)))[5:8])
    #typ
    print(str(re.findall(r"<td>\w*</td>", str(item), re.UNICODE))[6:-7])
    #nazev NOT WORKING
    print(re.findall(r"\">\w+? *?</a>", str(item), re.UNICODE))
    print()

#for item in tr:
    #print(item)
    #print("<hr>")


#tr = table.find_all('tr')
#for i in tr:
    #print(i)

#for row in table:
        #cells = row.find_all('td')

        #if (len(cells) >= 3):
        #        term = Termin(cells[0], cells[0].find('b').content, cells[1], cells[2])
        #        term.formatter()

        # print("\n")
        # print(cells)

# print()
