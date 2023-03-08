#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.environ['USE_PYGEOS'] = '0'
import geopandas as gpd
import osmnx as ox
import networkx as nx

graph = ox.load_graphml('graph.graphml')


# In[2]:


type(graph)


# In[3]:


graph


# In[4]:


ox.graph_to_gdfs(graph, nodes=True, edges=False)


# In[5]:


nodes = ox.graph_to_gdfs(graph, nodes=True, edges=False)
edges = ox.graph_to_gdfs(graph, nodes=False, edges=True)


# In[6]:


nodes.shape[0]


# In[7]:


edges


# In[8]:


edges.shape


# In[9]:


edges.shape[0]


# In[10]:


import os
import geopandas as gpd
import osmnx as ox
import networkx as nx

graph = ox.load_graphml('graph.graphml')


# In[11]:


type(graph)


# In[12]:


nodes.crs


# In[13]:


edges.head()


# In[14]:


edges['length'].min()


# In[15]:


edges['length'].max()


# In[16]:


edges['length'].mean()


# In[17]:


fig, ax = ox.plot_graph(graph, bgcolor='white', node_color='blue', edge_color='grey', node_size=5)


# In[18]:


import os
os.environ['USE_PYGEOS'] = '0'
import geopandas as gpd

cities = gpd.read_file('data/oregon_cities.shp')
cities.head()


# In[19]:


cities.crs


# In[20]:


cities_reproject = cities.to_crs('EPSG:32610')
cities_reproject.crs


# In[21]:


cities_reproject


# In[22]:


city1 = cities_reproject[cities_reproject['City'] == 'Adams']


# In[23]:


city2 = cities_reproject[cities_reproject['City'] == 'Adrian']


# In[24]:


city3 = cities_reproject[cities_reproject['City'] == 'Albany']


# In[25]:


city4 = cities_reproject[cities_reproject['City'] == 'Aloha']


# In[39]:


adams = cities_reproject[cities_reproject['City'] == 'Adams'].reset_index()
adrian = cities_reproject[cities_reproject['City'] == 'Adrian'].reset_index()
albany = cities_reproject[cities_reproject['City'] == 'Albany'].reset_index()
aloha = cities_reproject[cities_reproject['City'] == 'Aloha'].reset_index()


# In[40]:


dis1 = adams.distance(adrian).values[0] / 1000
dis1


# In[41]:


dis2 = adams.distance(albany).values[0] / 1000
dis2


# In[42]:


dis3 = adams.distance(aloha).values[0] / 1000
dis3


# In[43]:


dis4 = adrian.distance(albany).values[0] / 1000
dis4


# In[44]:


dis5 = adrian.distance(aloha).values[0] / 1000
dis5


# In[45]:


dis6 = albany.distance(aloha).values[0] / 1000
dis6


# In[46]:


adams_coord_x = city1["geometry"].x


# In[47]:


adams_coord_x


# In[48]:


adams_coord_y = city1["geometry"].y


# In[49]:


adams_coord_y


# In[50]:


adams_target_node = ox.distance.nearest_nodes(graph, X=adams_coord_x, Y=adams_coord_y, return_dist=False)[0]


# In[51]:


adams_target_node


# In[52]:


adrian_x = city2["geometry"].x


# In[53]:


adrian_y = city2["geometry"].y


# In[54]:


adrian_target_node = ox.distance.nearest_nodes(graph, X=adrian_x, Y=adrian_y, return_dist=False)[0]


# In[55]:


adrian_target_node


# In[56]:


albany_x = city3["geometry"].x


# In[57]:


albany_y = city3["geometry"].y


# In[58]:


albany_target_node = ox.distance.nearest_nodes(graph, X=albany_x, Y=albany_y, return_dist=False)[0]


# In[59]:


albany_target_node


# In[60]:


aloha_x = city4["geometry"].x


# In[61]:


aloha_y = city4["geometry"].y


# In[62]:


aloha_target_node = ox.distance.nearest_nodes(graph, X=aloha_x, Y=aloha_y, return_dist=False)[0]


# In[63]:


aloha_target_node


# In[64]:


# Calculate the shortest path
route3 = nx.shortest_path(graph, source=albany_target_node , target=aloha_target_node, weight='length')
length = nx.shortest_path_length(graph, source=albany_target_node, target=aloha_target_node, weight='length')
print("Shortest path distance = {t:.1f} km.".format(t=length/1000))


# In[65]:


print("Shortest path distance = {t:.1f} km.".format(t=length/1000))


# In[66]:


# Calculate the shortest path
route2 = nx.shortest_path(graph, source=albany_target_node, target=adrian_target_node, weight='length')
length = nx.shortest_path_length(graph, source=albany_target_node, target=adrian_target_node, weight='length')
print("Shortest path distance = {t:.1f} km.".format(t=length/1000))


# In[67]:


print("Shortest path distance = {t:.1f} km.".format(t=length/1000))


# In[68]:


# Calculate the shortest path
route1 = nx.shortest_path(graph, source=albany_target_node, target=adams_target_node, weight='length')
length = nx.shortest_path_length(graph, source=albany_target_node, target=adams_target_node, weight='length')
print("Shortest path distance = {t:.1f} km.".format(t=length/1000))


# In[69]:


fig, ax = ox.plot_graph_route(graph, route1)


# In[70]:


fig, ax = ox.plot_graph_route(graph, route2)


# In[71]:


fig, ax = ox.plot_graph_route(graph, route3)


# In[72]:


cities_reproject


# In[74]:


edges.head()


# In[76]:


travel_speed = 60
meters_per_minute = travel_speed * 1000 / 60  # km per hour to m per minute

for u, v, data in graph.edges.data():
    data['time'] = data['length'] / meters_per_minute


# In[77]:


list(graph.edges.data())[0]


# In[ ]:




