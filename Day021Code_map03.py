#100DaysOfCode 021/100 - Building a map day 03
#   2020-07-04
#
#  20200703 - Because day 19 was short I will leave day 19 here and add to the code and notes
#               Python has optional libraties to keep it light.
#               pip3 install folium
#  20200704 - This is a continuation of day 20.
#                Adding a pointer didnd't work - trouble shooting
#
#
import folium
#   I am using the terminal for the interactive shell for this exercise
#      I am using this file for notes and to save the progam
#   use dir(folium) to get a list of objects
#      help(folium.map) --- will show what can be passed to the map object
#    scroll there is a lot of infor there
#     Q - to exit help
#
#  Carlisle latitude  =  40.201452
#           longitude = -77.201452
#
#  Create a map object
#      This is a layer - other layers can be added
#map_object = folium.Map(location=[40.2011,-77.2498], zoom_start=8, tiles="Stamen Terrain")
map_object = folium.Map(location=[40.201452,-77.201452], zoom_start=10)
#  maps are created in HTML format
#  elements can be saved to the map
#      in this case a marker will be added
#
#  the following line is not working from the lesson --- start googling
#map_object.add_child(folium.Marker(location=[40.20,-77.24], popup="hi I am a Marker", icon=folium.Icon(color='green')))
#map_object.add_child(folium.Marker(location=[40.20,-77.201452], popup="Carlisle is here", icon=folium.Icon(colors='green')))
#  The instructor added some code in prep for the next lession - I am modifying
#     my program then trouble shooting
#  Add the icon to a function group - to keep code clean for later lessons
map_fg = folium.FeatureGroup("Carlisle Map")
map_fg.add_child(folium.Marker(location=[40.201452,-77.201452], popup="Carlisle is here", icon=folium.Icon(colors='green')))
map_object.add_child(map_fg)
#
#save the map object
#    Note - don't forget when working in the python shell the default directory
#      is used.  When executing the python code here a file path is needed
#      if you want to use a specific file folder
map_object.save("files/mapping/Home_Map.html")
#  the rile path for the browser is -- file:///home/karl/python/files/mapping/Home_Map.html
