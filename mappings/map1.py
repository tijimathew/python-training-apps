import folium
map = folium.Map(location=[34, 15], zoom_start=6, tiles="Stamen Terrain")

map.add_child(folium.Marker(location=[34.1, 15.1], popup="Hi I am a marker", icon=folium.Icon(color='green')))

map.save("map1.html")