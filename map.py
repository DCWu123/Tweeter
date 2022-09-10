# Libraries to map the data
import folium 

# Creating a map
Latitud=9.74722222
Longitud=-84.14527778
canton = 'aserri'
x=9.75722999
y=-84.15527800
map = folium.Map(location=[Latitud,Longitud ], zoom_start=12)
# Adding markers
map.add_child(folium.Marker(location=[Latitud,Longitud], popup=canton, icon=folium.Icon(color='red' , icon='')))
# Adding markers
map.add_child(folium.Marker(location=[x,y], popup=canton, icon=folium.Icon(color='red' , icon='cloud')))

# showing the map
map.save('map.html')