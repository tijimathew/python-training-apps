import folium
mylocation = [34.133159, -84.144573]

map = folium.Map(location=mylocation, zoom_start=8, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
for coordinates in [[34.1, 15.1],[36.1, 17.1],[34.133159, -84.144573]]:
    fg.add_child(folium.Marker(location=coordinates , popup="Coordinates : %s, %s " % (coordinates[0], coordinates[1]), icon=folium.Icon(color='pink')))


map.add_child(fg)

map.save("map1.html")