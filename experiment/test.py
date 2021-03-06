import folium
import pandas
from math import floor
##basic
map_osm = folium.Map(location=(24.298193, 120.524229), zoom_start=15, tiles='Stamen Terrain ')
# folium.Marker([24.31005, 120.525602], popup='place A').add_to(map_osm)
a = folium.Marker((24.296555, 120.523988))
folium.CircleMarker((24.297985, 120.525100), radius=20,  color='#ff6699',
                    fill_color='#ff6699').add_to(map_osm)
folium.LatLngPopup().add_child(a).add_to(map_osm)
# folium.LatLngPopup().add_to(map_osm)
map_osm.save('osm.html')
##icon
map_1 = folium.Map(location=[45.372, -121.6972], zoom_start=12,tiles='Stamen Terrain')
folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows',
                   icon = folium.Icon(icon = 'cloud')).add_to(map_1)
folium.Marker([45.3311, -121.7113], popup='Timberline Lodge',
                   icon = folium.Icon(color ='green')).add_to(map_1)
folium.Marker([45.3300, -121.6823], popup='Some Other Location',
                   icon = folium.Icon(color ='red')).add_to(map_1)
map_1.save('iconTest.html')

##altitude practice
m = folium.Map(location = [25.044769, 121.537016], zoom_start = 10, tiles = 'Cartodb Positron')

data = pandas.read_csv("example.txt")
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])
hgt = list(data["ALTITUDE"])
# data_list = [
#              {'coordinate':[24.296555,120.523988],'height':245},
#              {'coordinate':[24.296431,120.546988],'height':315},
#              {'coordinate':[24.310892,120.531988],'height':785},
#              {'coordinate':[24.302456,120.563188],'height':458},
#              {'coordinate':[24.293564,120.543978],'height':123},
#              {'coordinate':[24.291568,120.575988],'height':653}
# ]
color = ['#66ccff','#3399ff','#0066ff','#0000ff','#000099','#000066']

fgm = folium.FeatureGroup(name="Mountains")
for lat,lon,hgt in zip(lat,lon,hgt):
    colorPick = floor(hgt/200)
    fgm.add_child(folium.RegularPolygonMarker(location = [lat, lon],
                                popup = str(hgt)+" m",
                                number_of_sides = 3,
                                rotation = 30,
                                radius = 15,
                                color ='#deebf7',
                                fill_color = color[colorPick],
                                fill_opacity = 0.5))
fgm.add_to(m)

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data =(open("world.json", 'r',encoding = 'utf-8-sig')),
                            style_function = lambda x : {'fillColor':'#ff9933' if x["properties"]["POP2005"] > 100000000
                                                            else '#ffff99' if 1000000 <= x['properties']['POP2005'] <= 10000000
                                                            else '#66ccff' } ))
fgp.add_to(m)

m.add_child(folium.LayerControl(position = 'topright'))
m.save('point.html')
