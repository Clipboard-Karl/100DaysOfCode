#100DaysOfCode 0xx/100 - This is the file that contains my python mapping
#     assignment.  It took some trouble shooting however I am now running from
#     my local GitHub clone.  So GitHub will be my version control and not
#     me renaming files and saving.
#     This could us a major clean up an organization but for now I am focued on
#     learning the code.  Maybe later.
#
#
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
#  import folium to to build a map
import folium
#  in the python interactive shell:
#    use dir(folium) to get a list of objects
#      help(folium.map) --- will show what can be passed to the map object
#    scroll there is a lot of infor there
#     Q - to exit help
#
#  Carlisle latitude  =  40.201452
#           longitude = -77.201452
#
#  Create a map object
#      This is a layer - other layers can be added
#-----------------------------
#  The next line will center and zoom on Carlisle
#map_object = folium.Map(location=[40.201452,-77.201452], zoom_start=12)
#  This will center on the US
map_object =folium.Map(location=[39.09,-94.85], zoom_start=5)
#-----------------------------
#  Map styles can be changed with the tiles parameter
#  This next line is directly from the lesson and does not point to carlisle
#-----------------------------
#map_object = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")
#-----------------------------
#  maps are created in HTML format
#  elements can be saved to the map
#      in this case a marker will be added
#
#  Add the icon to a function group - to keep code clean for later lessons
map_fg = folium.FeatureGroup("Carlisle Map")
#  Elements can be saved to the map
#      The next lines will add a markers
#---------------------------
map_fg.add_child(folium.Marker(location=[40.201452,-77.201452], popup="Carlisle is here", icon=folium.Icon(color='green')))
map_fg.add_child(folium.Marker(location=[40.2023587,-77.2065121], popup="Leo's", icon=folium.Icon(color='green')))
#---------------------------
#  markers can be added with a for loop itteration
for marker_coordinates in [[40.25,-77.25],[40.3,-77.1]]:
    map_fg.add_child(folium.Marker(location=marker_coordinates, popup="For Loop", icon=folium.Icon(color="orange")))
#
#  The following code will read a .txt file to add markers
import pandas
#  create a DataFrame from the file
volcano_data = pandas.read_csv("Files/Mapping/Volcanoes.txt")
#  create lists from the DataFrame
#     working on a list is faster than wroking with a DataFrame
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
#  HTML can be added to the Popup - this will allow a google search of the name
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Elevation: %s m
"""
#
#  iterate throught the lists with the zip function
for lt, ln, el, name in zip(volcano_lat, volcano_lon, volcano_elev, volcano_name):
#  the popup parameter is expecting a string. This didn't error however I will
#  convert the float to a string
#    map_fg.add_child(folium.Marker(location=[lt, ln], popup="Elevation: "+str(el), icon=folium.Icon(color="red")))
#
#     the follow is for adding HTML to the Popup
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    map_fg.add_child(folium.CircleMarker(location=[lt, ln],
                                         radius = 6,
                                         popup=folium.Popup(iframe),
                                         fill_color=color_producer(el),
                                         color = 'gray',
                                         fill_opacity=0.7,
                                         fill=True))
#
map_object.add_child(map_fg)
#
#save the map object
#    Note - don't forget when working in the python shell the default directory
#      is used.  When executing the python code here a file path is needed
#      if you want to use a specific file folder
map_object.save("Files/Mapping/Home_Map.html")
#  My browser paath is -- file:///home/karl/python/files/mapping/Home_Map.html
