#100DaysOfCode 019/100 - Building a map
#   2020-07-02
#
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
map_object = folium.Map(location=[40.2011,-77.2498], zoom_start=6)
#  maps are created in HTML format
#  save the map object
#    Note - don't forget when working in the python shell the default directory
#      is used.  When executing the python code here a file path is needed
#      if you want to use a specific file folder
map_object.save("files/mapping/Home_Map.html")
