import folium
import pandas as pd
#mylocation = [34.133159, -84.144573]
data = pd.read_csv('volcanoes.txt')

html = """
<h4>Volcano Name:</h4> 
<a href="https://www.google.com/search?q=%%22Volcanoes%%22+%%22%s%%22" target="_blank">%s</a><br>
Type: %s<br>
Elevation: %s
"""

# Create two lists - one with latitudes and one with longitudes
lat = list(data['LAT'])
lon = list(data['LON'])
vol_elev = list(data['ELEV'])
vol_name = list(data['NAME'])
vol_type = list(data['TYPE'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation >=1000 and elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[lat[0], lon[0]], zoom_start=8, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
for lt, ln, vel, vnam, vtyp in zip(lat, lon, vol_elev, vol_name, vol_type):
    iframe = folium.IFrame(html=html % (vnam, vnam, vtyp, str(vel)), width=300, height=200)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(vel))))


map.add_child(fg)

map.save("map_advanced_color.html")