import folium
import pandas as pd
#mylocation = [34.133159, -84.144573]
data = pd.read_csv('volcanoes.txt')

# Create two lists - one with latitudes and one with longitudes
lat = list(data['LAT'])
lon = list(data['LON'])
vol_num = list(data['NUMBER'])
vol_name = list(data['NAME'])
vol_type = list(data['TYPE'])

map = folium.Map(location=[lat[0], lon[0]], zoom_start=8, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
for lt, ln, vnum, vnam, vtyp in zip(lat, lon, vol_num, vol_name, vol_type):
    popup_lbl = "<strong>Number</strong>: %s<br>Name: %s<br>Type: %s" % (str(vnum), vnam, vtyp)
    fg.add_child(folium.Marker(location=[lt, ln], popup=popup_lbl, icon=folium.Icon(color='pink')))


map.add_child(fg)

map.save("map1.html")