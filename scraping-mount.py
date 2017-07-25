from bs4 import BeautifulSoup
import urllib
# import pandas
from pyproj import Proj

request = urllib.request.urlopen('http://www.mountaineering.org.tw/tw/index.php/2015-09-13-14-48-49/2015-09-13-15-07-13').read()
soup = BeautifulSoup(request, "html.parser")


myProj = Proj("+proj=tmerc +ellps=GRS67 +lon_0=121 +x_0=250000 +k=0.9999 +units=m +no_defs")
fs = open('mount-data.txt','w', encoding="utf-8")
fs.seek(0)
trs = soup.find_all('tr')
first = trs[1]
keys = []
for td in first.find_all('td'):
    keys.append(td.text.replace("\n","").replace(" ",""))

fs.write("name,latitude,longitude,altitude\n")
data = []
trs.reverse()
for tr in trs[2::]:
    d = {}
    tds = tr.find_all('td')
    try:
        name = tds[1].text.replace("\n","").replace(" ","")
        x = tds[2].text.replace("\n","").replace(" ","")
        y = tds[3].text.replace("\n","").replace(" ","")
        longt, lat = myProj(x, y, inverse=True)
        alt = tds[4].text.replace("\n","").replace(" ","").replace("公尺","")
        fs.write('%s,%s,%s,%s\n' %(name, lat, longt, alt))
    except:
        pass
fs.close()
