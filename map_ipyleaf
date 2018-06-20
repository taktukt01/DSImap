from ipywidgets import HTML
from ipyleaflet import Map, Marker, Popup,basemaps, basemap_to_tiles


#map
map = Map(center = [19.087991, -71.715163] , zoom = 9)
place = [19.097991, -71.715163]
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)

#popup
message = HTML()
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place,
    
    close_button = True
    
)
sample_layer = basemap_to_tiles(basemaps.Stamen.Terrain)



map.add_layer(popup)
map.add_layer(sample_layer)
marker.popup = message
map
