from ipywidgets import HTML
from ipyleaflet import Map, Marker, Popup

#construction of MAP
map = Map(center = [19.087991, -71.715163] , zoom = 8)
place = [19.097991, -71.715163]
#construction of MARKER
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)

#construction of popUP
message = HTML()
message.value = "Point of convergence : marketplace: Dajabon"
popup = Popup(
    location = place,
    close_button = False,
    keep_in_view = True
    
)
map.add_layer(popup)
marker.popup = message

map
