#100DaysOfCode 022/100 - Clean up the map code
#   2020-07-05
#
#
#  20200705 - Cleaning the code
#  20200704 - This is a continuation of day 20.
#                Adding a pointer didnd't work - trouble shooting
#                Result - I found a missing negitive sign on my longitude
#  20200703 - Because day 19 was short I will leave day 19 here and add to the
#               code and notes
#               Python has optional libraties to keep it light.
#               pip3 install folium
#
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
map_object = folium.Map(location=[40.201452,-77.201452], zoom_start=10)
#  Map styles can be changed with the tiles parameter
#map_object = folium.Map(location=[40.201452,-77.201452], zoom_start=8, tiles="Stamen Terrain")
#  maps are created in HTML format
#  elements can be saved to the map
#      in this case a marker will be added
#
#  Add the icon to a function group - to keep code clean for later lessons
map_fg = folium.FeatureGroup("Carlisle Map")
#  Elements can be saved to the map
#      The next line will add a marker
map_fg.add_child(folium.Marker(location=[40.201452,-77.201452], popup="Carlisle is here", icon=folium.Icon(colors='green')))
map_object.add_child(map_fg)
#
#save the map object
#    Note - don't forget when working in the python shell the default directory
#      is used.  When executing the python code here a file path is needed
#      if you want to use a specific file folder
map_object.save("files/mapping/Home_Map.html")
#  My browser paath is -- file:///home/karl/python/files/mapping/Home_Map.html
