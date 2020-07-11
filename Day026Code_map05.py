#100DaysOfCode 0xx/100 - This is the file that contains my python mapping
#     assignment.  It took some trouble shooting however I am now running from
#     my local GitHub clone.  #
#
#  20200711 - 100DaysOfCode 026/100 - Completed pythin with openstreetmaps
#             First I copied this code from Day023Code_map04 and cleaned it.
#             With all the lesson notes this is not streamlined but it works for me.
#  20200710 - 100DaysOfCode 025/100 - Popup windows on maps
#                Adding logic for marker color
#  20200708 - 100DaysOfCode 024/100 - Adding points form a .txt file
#             The color was not changing because I was using colors not colors
#             I am concerned that the .txt file would need error checking first
#  20200707 - Adding points to the map
#  20200705 - Cleaning the code
#  20200704 - This is a continuation of day 20.
#                Adding a pointer didnd't work - trouble shooting
#                Result - I found a missing negitive sign on my longitude
#  20200703 - Because day 19 was short I will leave day 19 here and add to the
#               code and notes
#               Python has optional libraties to keep it light.
#               pip3 install folium
#
#  Notes:  This uses openstreetmaps.org
################################################################################
#  import folium and use it to build a map
import folium
#  pandas - data analysis and minipulation tool
import pandas
#
#  Create a DataFrame from the Volcanoes.txt file
volcano_data = pandas.read_csv("Files/Mapping/Volcanoes.txt")
#  Create lists from the DataFrame
#     Reason - working on a list is faster than wroking with a DataFrame
#   Karl Note:  I don't like this - unless I am missing something this is assuming
#               the .txt file has no erros or missing numbers.  Maybe more will
#               be said about this later - or the file was validated ??????
volcano_lat = list(volcano_data["LAT"])
volcano_lon = list(volcano_data["LON"])
volcano_elev = list(volcano_data["ELEV"])
volcano_name = list(volcano_data["NAME"])
#
#  This function will adjust volcano icon colors based on Elevation
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
#
#  Carlisle latitude  =  40.201452
#           longitude = -77.201452
#
#  Create a map object
#      This is a layer - other layers can be added
#-----------------------------
#  The next line will center and zoom on Carlisle
#map_object = folium.Map(location=[40.201452,-77.201452], zoom_start=16)
#  This will center on the US
map_object =folium.Map(location=[39.09,-94.85], zoom_start=5)
#  Map styles can be changed with the tiles parameter
#map_object = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")
#-----------------------------
#  maps are created in HTML format
#
################################################################################
#
#  This section will add a point features group to the map
#
#  Add the icon to a function group - to keep code clean for later lessons
map_fg_carlisle = folium.FeatureGroup("Carlisle Map")
#  Elements can be saved to the map
#      The next lines will add a markers for Carlisle
#---------------------------
map_fg_carlisle.add_child(folium.Marker(location=[40.2015,-77.189277],
                               popup="Carlisle is here",
                               icon=folium.Icon(color='green')))
map_fg_carlisle.add_child(folium.Marker(location=[40.2023587,-77.2065121],
                               popup="Leo's",
                               icon=folium.Icon(color='green')))
#---------------------------
#  Example of adding markers with a for loop iteration
for marker_coordinates in [[40.25,-77.25],[40.3,-77.1]]:
    map_fg_carlisle.add_child(folium.Marker(location=marker_coordinates,
                                   popup="For Loop",
                                   icon=folium.Icon(color="orange")))
#  Add a US volcano feature group
map_fg_volcanos = folium.FeatureGroup("Volcano Map")
#  HTML can be added to the Popup - this will allow a google search of the name
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Elevation: %s m
"""
#  iterate throught the lists with the zip function to keep lists in sync
for lt, ln, el, name in zip(volcano_lat, volcano_lon, volcano_elev, volcano_name):
#  Possible error note popup parameter expects a string. This didn't error however I will
#  convert the float to a string with popup="Elevation: "+str(el)
#
#  The IFrame will add the above HTML to the Popup
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    map_fg_volcanos.add_child(folium.CircleMarker(location=[lt, ln],
                                         radius = 6,
                                         popup=folium.Popup(iframe),
                                         fill_color=color_producer(el),
                                         color = 'gray',
                                         fill_opacity=0.7,
                                         fill=True))
#
################################################################################
#
# This sectoin will add a polygon feactures group to the map
map_fg_population = folium.FeatureGroup("Population Map")
#
map_fg_population.add_child(folium.GeoJson(data=open('Files/Mapping/world.json','r',
                                           encoding='utf-8-sig').read(),
                                          style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                          else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red' }))
#
#
################################################################################
#
#  add layer control
#     Layer controll requires the feature groups to be added
#
map_object.add_child(map_fg_carlisle)
map_object.add_child(map_fg_volcanos)
map_object.add_child(map_fg_population)
map_object.add_child(folium.LayerControl())


################################################################################
#map_object.add_child(map_fg)
#
#save the map object
#    Note - don't forget when working in the python shell the default directory
#      is used.  When executing the python code here a file path is needed
#      if you want to use a specific file folder
map_object.save("Files/Mapping/Home_Map.html")
#  My browser path is -- file:///home/karl/python/files/mapping/Home_Map.html
