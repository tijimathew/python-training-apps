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

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, vel, vnam, vtyp in zip(lat, lon, vol_elev, vol_name, vol_type):
    iframe = folium.IFrame(html=html % (vnam, vnam, vtyp, str(vel)), width=300, height=200)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=8, popup=folium.Popup(iframe), 
    fill_color=color_producer(vel), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl()) # add layer control after adding feature group to map.

map.save("map_advanced_color.html")