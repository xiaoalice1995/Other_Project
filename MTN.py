# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:45:10 2020

@author: Shirley
"""

import requests
from bs4 import BeautifulSoup
from pandas import Series,DataFrame
import pandas as pd
import re
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic = {}
dic['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df = pd.DataFrame(dic)
df
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_1.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)

url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_2.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_3.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_4.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_5.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_6.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_7.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_8.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_9.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_10.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_11.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_12.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_13.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_14.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_15.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_16.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_17.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_18.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_19.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_20.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_21.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_22.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_23.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_24.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_25.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_26.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_27.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_28.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_29.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_30.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_31.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_32.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_33.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_34.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_35.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_36.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_37.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_38.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_39.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_40.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_41.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_42.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_43.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_44.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_45.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_46.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_47.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_48.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
url = 'http://www.nafmii.org.cn/dcmfx/tzs/mtn/index_49.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
dic1 = {}
dic1['标题及链接'] = soup.find_all('td', width="649", height="25", align="left")
dic1['日期'] = soup.find_all('td', align="center", class_="font_hui", style="font-family:'宋体'", width="83")
df1 = pd.DataFrame(dic1)
df1
df = df.append(df1)
df.shape
outputpath='c:/Users/Shirley/Desktop/MTN.xlsx'
df.to_excel(outputpath,index=False,header=True)
