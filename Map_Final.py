
# coding: utf-8

# In[3]:


from ipyleaflet import (Map,Marker)


# In[4]:


map = Map(center = [19.087991, -71.715163] , zoom = 8)


# In[5]:


marker = Marker( location = [19.097991, -71.715163]  , draggable = False)


# In[6]:


map.add_layer(marker)


# In[7]:


map


# In[8]:


marker2 = Marker(location = [19.087991, -70.715163] , draggable = False)


# In[9]:


map.add_layer(marker2)


# In[10]:


map


# In[11]:


message = HTML()
message.value = "This is the marketplace Dajabon"


# In[12]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup


# In[13]:


message = HTML()
message.value = "This is the marketplace Dajabon"


# In[14]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup
map = Map(center = [19.087991, -71.715163] , zoom = 8)
place = [19.097991, -71.715163]
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)
message = HTML()
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place
    child = message
    close_button = False
    
)
map.add_layer(popup)
marker.popup = message


# In[15]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup
map = Map(center = [19.087991, -71.715163] , zoom = 8)
place = [19.097991, -71.715163]
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)
message = HTML()
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place
    child = "Hello"
    close_button = False
    
)
map.add_layer(popup)
marker.popup = message


# In[16]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup
map = Map(center = [19.087991, -71.715163] , zoom = 8)
place = [19.097991, -71.715163]
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)
message = HTML()
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place,
    child = "Hello",
    close_button = False
    
)
map.add_layer(popup)
marker.popup = message


# In[17]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup
map = Map(center = [19.087991, -71.715163] , zoom = 8)
place = [19.097991, -71.715163]
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)
message = HTML()
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place
    child = message
    close_button = False
    
)
map.add_layer(popup)
marker.popup = message


# In[18]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup
map = Map(center = [19.087991, -71.715163] , zoom = 8)
place = [19.097991, -71.715163]
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)
message = HTML()
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place
    close_button = False
    
)
map.add_layer(popup)
marker.popup = message


# In[19]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup
map = Map(center = [19.087991, -71.715163] , zoom = 8)
place = [19.097991, -71.715163]
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)
message = HTML()
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place,
    close_button = false
    
)
map.add_layer(popup)
marker.popup = message


# In[20]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup
map = Map(center = [19.087991, -71.715163] , zoom = 8)
place = [19.097991, -71.715163]
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)
message = HTML()
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place,
    
    close_button = False
    
)
map.add_layer(popup)
marker.popup = message


# In[21]:


map


# In[22]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup
map = Map(center = [19.087991, -71.715163] , zoom = 8)
place = [19.097991, -71.715163]
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)
message = HTML()
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place,
    
    close_button = False
    
)
map.add_layer(popup)
marker.popup = message


# In[23]:


map


# In[24]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup
map = Map(center = [19.087991, -71.715163] , zoom = 9)
place = [19.097991, -71.715163]
marker = Marker( location = place  , draggable = False)
map.add_layer(marker)
message = HTML()
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place,
    
    close_button = False
    
)
map.add_layer(popup)
marker.popup = message


# In[25]:


map


# In[26]:


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
message.value = "This is the marketplce Dajabon"
popup = Popup(
    location = place,
    close_button = False,
    keep_in_view = False
    
)
map.add_layer(popup)
marker.popup = message


# In[27]:


map


# In[28]:


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


# In[29]:


map

