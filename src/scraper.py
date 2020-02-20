#!/bin/python

import requests
import re

from bs4 import BeautifulSoup

from src.config import Config
from src.termin import Termin

cfg = Config()
page = requests.get("https://wis.fit.vutbr.cz/FIT/st/news-c.php",
                    verify=False,
                    auth=(cfg.get_login(), cfg.get_password()))
page_content = BeautifulSoup(page.content, "html.parser")
table = page_content.find_all(attrs={"bgcolor":"#dfe7cf"}) +
                              page_content.find_all(attrs={"bgcolor":"#FFF8DC"})

termin_list = []

print("-----------------------------------------------------------------------")
for row in table:
    # WIS IS RETARDED, date might be out of range
    date = re.findall(r"([0-9]{4}-[0-9]{2}-[0-9]{2}|dnes|zítra)<", str(row))
    date_start_end = re.findall(r"([0-9]{4}-[0-9]{2}-[0-9]{2}|dnes) ([0-9]{2}:[0-9]{2}:[0-9]{2})", str(row))
    subject = str(re.findall(r"<b>[A-Z0-9]{3}</b>", str(row)))[5:8]
    term_type = str(re.findall(r"<td>\w*</td>", str(row), re.UNICODE))[6:-7]
    name = str(re.findall(r"(\">[A-Z]\w.*</a>)", str(row), re.UNICODE))[4:-6]

    if len(date_start_end) == 2:
        date_start = date_start_end[0][0] + " " + date_start_end[0][1]
        date_end = date_start_end[1][0] + " " + date_start_end[1][1]
        print(date[0], " | ", subject, " | ", term_type, " | ", name, " | ", date_start, "|", date_end)
    elif len(date) == 1:
        date_start = None
        date_end = None
        print(date[0], " | ", subject, " | ", term_type, " | ", name)
    else:
        print("YOURE DRUNK WIS, GO HOME")
        exit(666)

    print("-------------------------------------------------------------------")
    termin = Termin(date, subject, name, term_type, date_start, date_end)
    termin_list.append(termin)