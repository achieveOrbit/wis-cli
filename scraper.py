#!/bin/python
import requests
import re
from bs4 import BeautifulSoup

from config import Config

cfg = Config()

page = requests.get("https://wis.fit.vutbr.cz/FIT/st/news-c.php", verify=False, auth=(cfg.get_login(), cfg.get_password()))
page_content = BeautifulSoup(page.content, "html.parser")
table = page_content.find_all(attrs={"bgcolor":"#dfe7cf"}) + page_content.find_all(attrs={"bgcolor":"#FFF8DC"})


for row in table:
    date = re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", str(row))
    subject = str(re.findall(r"<b>[A-Z0-9]{3}</b>", str(row)))[5:8]
    term_type = str(re.findall(r"<td>\w*</td>", str(row), re.UNICODE))[6:-7]
    name = str(re.findall(r"(\">[A-Z]\w.*</a>)", str(row), re.UNICODE))[4:-6]
    #print(date[0], " | ", subject, " | ", term_type, " | ", name, "\n")