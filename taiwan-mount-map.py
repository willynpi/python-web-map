import pandas
import folium
from math import floor

mount_map = folium.Map([23.770876, 120.934757], zoom_start=8, tiles='Cartodb Positron')
data = pandas.read_csv("example.txt")
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])
hgt = list(data["ALTITUDE"])

color = ['#66ccff','#3399ff','#0066ff','#0000ff','#000099','#000066']
for lat,lon,hgt in zip(lat,lon,hgt):
    colorPick = floor(hgt/300)
    popup = str(hgt)+" m"
    folium.RegularPolygonMarker([lat, lon, hgt],
                                popup=popup,
                                number_of_sides=3,
                                rotation=30,
                                radius=15 ,
                                color='#deebf7',
                                fill_color=color[colorPick],
                                fill_opacity=0.5).add_to(mount_map)
mount_map.save('mount-map-TW.html')
