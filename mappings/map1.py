import folium
import pandas as pd
mylocation = [34.133159, -84.144573]
data = pd.read_csv('volcanoes.txt')

# Create two lists - one with latitudes and one with longitudes
lat = list(data['LAT'])
lon = list(data['LON'])

map = folium.Map(location=mylocation, zoom_start=8, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Coordinates : %s, %s " % (lt, ln), icon=folium.Icon(color='pink')))


map.add_child(fg)

map.save("map1.html")