import folium
map = folium.Map(location=[34, 15], zoom_start=6, tiles="Stamen Terrain")
map.save("map1.html")