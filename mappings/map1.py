import folium
import pandas as pd
#mylocation = [34.133159, -84.144573]
data = pd.read_csv('volcanoes.txt')

html = """
Volcano Name: 
<a href="https://www.google.com/search?q=%%22Volcanoes%%22+%%22%s%%22" target="_blank">%s</a><br>
Type: %s
"""

# Create two lists - one with latitudes and one with longitudes
lat = list(data['LAT'])
lon = list(data['LON'])
vol_name = list(data['NAME'])
vol_type = list(data['TYPE'])

map = folium.Map(location=[lat[0], lon[0]], zoom_start=8, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
for lt, ln, vnam, vtyp in zip(lat, lon, vol_name, vol_type):
    iframe = folium.IFrame(html=html % (vnam, vnam, vtyp), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='pink')))


map.add_child(fg)

map.save("map_advanced.html")