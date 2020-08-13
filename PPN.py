# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:45:54 2020

@author: Shirley
"""

import requests
from bs4 import BeautifulSoup
from pandas import Series,DataFrame
import pandas as pd
import re
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic={"title": title, "link_address": link_address, "date": date}
df = pd.DataFrame(dic)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_1.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_2.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_3.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_4.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_5.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_6.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_7.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_8.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_9.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_10.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_11.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_12.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_13.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_14.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_15.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_16.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_17.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_18.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_19.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_20.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_21.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_22.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_23.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_24.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_25.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_26.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_27.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_28.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_29.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_30.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_31.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_32.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_33.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_34.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_35.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_36.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_37.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_38.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_39.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_40.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_41.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_42.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_43.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_44.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_45.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_46.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_47.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_48.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/ppn/index_49.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
title = []
ttllist = soup.find_all('td', width="649", height="25", align="left")
for ttl in ttllist:
    ttl.get_text()
    title.append(ttl.get_text())
link_address = []
urls_tr = soup.find_all('td', width="649", height="25", align="left")
for url_tr in urls_tr:
    urls_href = url_tr.select("a")
    for url_href in urls_href:
        url_ppn = url_href.get("href")
        url_ppn = url_ppn.replace('./','')
        link_address.append('http://www.nafmii.org.cn/dcmfx/tzs/ppn/'+url_ppn)
date = []
dtlist = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
for dt in dtlist:
    dt.get_text()
    date.append(dt.get_text())
dic1={"title": title, "link_address": link_address, "date": date}
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
df.shape

outputpath='c:/Users/Shirley/Desktop/PPN.xlsx'
df.to_excel(outputpath,index=False,header=True)