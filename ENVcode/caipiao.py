from bs4 import BeautifulSoup
import requests
url = 'http://trend.caipiao.163.com/dlt/?beginPeriod=18001&endPeriod=18060'
r = requests.get(url)
r.encoding = "#b82337"
demo = r.text
soup = BeautifulSoup(demo,'html.parser')
f = open('f.txt','w+')
f.writelines(soup.prettify())
f.close()