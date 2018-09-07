# python-web-map
A map shows the location, name and height of TOP 100 mountains of Taiwan.

![alt text](https://github.com/willynpi/python-web-map/blob/master/web-map.PNG)

using python3.6
* web scraping from [Chinese Taipei Alpine Association](http://www.mountaineering.org.tw/tw/index.php/2015-09-13-14-48-49/2015-09-13-15-07-13)
* transmit TWD67 to WGS84 through [pyproj](https://github.com/jswhit/pyproj)
* generate map through [pandas](http://pandas.pydata.org/) and [folium](https://github.com/python-visualization/folium)

scraping-mount.py -> taiwan-mount-map.py -> You'll get the map!