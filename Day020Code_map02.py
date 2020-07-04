#100DaysOfCode 020/100 - Building a map day 02
#   2020-07-03
#
#      side note - I need to look at GitHub - it may handle the revison better
#           Manually revising files is probably old school but for now I will
#           focus on learning the code.
#
#  Because day 19 was short I will leave day 19 here and add to the code and notes
#  Python has optional libraties to keep it light.
#     pip3 install folium
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
#  Home latitude  =  40.20112601118214
#       longitude = -77.24983399605837
#
#  Create a map object
#      This is a layer - other layers can be added
#map_object = folium.Map(location=[40.2011,-77.2498], zoom_start=8, tiles="Stamen Terrain")
map_object = folium.Map(location=[10.2011,-77.2498], zoom_start=8)
#  maps are created in HTML format
#  elements can be saved to the map
#      in this case a marker will be added
map_object.add_child(folium.Marker(location=[40.20,77.24], popup="hi I am a Marker", icon=folium.Icon(color='green')))
#
#save the map object
#    Note - don't forget when working in the python shell the default directory
#      is used.  When executing the python code here a file path is needed
#      if you want to use a specific file folder
map_object.save("files/mapping/Home_Map.html")
#  the rile path for the browser is -- file:///home/karl/python/files/mapping/Home_Map.html
