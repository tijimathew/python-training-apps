import folium
mylocation = [34.133159, -84.144573]

map = folium.Map(location=mylocation, zoom_start=14, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=mylocation, popup="Close to Home", icon=folium.Icon(color='pink')))
map.add_child(fg)

map.save("map1.html")