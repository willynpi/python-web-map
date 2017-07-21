import pandas
import folium
from math import floor

mount_map = folium.Map([23.770876, 120.934757], zoom_start=8, tiles='Cartodb Positron')
data = pandas.read_csv("mount-data.txt")
lat = list(data["latitude"])
lon = list(data["longitude"])
hgt = list(data["altitude"])
name = list(data["name"])

color = ["#77FF00","#00DD00","#00AA00","#668800","#BB5500","#886600"]
for name,lat,lon,hgt in zip(name,lat,lon,hgt):
    if hgt > 3000 :
        colorPick = floor((hgt-3000)/300)+1
    else :
        colorPick = 0
    html = "<div style=\"font-size:8px\"><p><strong>"+str(name)+ "</strong></p><p>"+str(hgt)+" m</p></div>"
    iframe = folium.IFrame(html = html, width=90, height=80)
    popup = folium.Popup(iframe, max_width=200)
    folium.RegularPolygonMarker([lat, lon, hgt],
                                popup=popup,
                                number_of_sides=3,
                                rotation=30,
                                radius=15 ,
                                color='#deebf7',
                                fill_color=color[colorPick],
                                fill_opacity=0.5).add_to(mount_map)
mount_map.save('mount-map-TW.html')
