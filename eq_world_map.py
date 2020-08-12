import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'

with open(filename) as f:
    all_equal = json.load(f)


readable = 'data/Readable_eq_data_30_day_.json'

with open(readable,'w') as file:
    json.dump(all_equal,file, indent = 4)


all_eq_dict = all_equal['features']

#print(len(all_eq_dict))

mags, longs, lats,hover_texts = [] , [] , [], []
for eq_data in all_eq_dict:
    data = eq_data['properties']['mag']
    long_data = eq_data['geometry']['coordinates'][0]
    lat_data = eq_data['geometry']['coordinates'][1]
    title= eq_data['properties']['title']
    mags.append(data)
    longs.append(long_data)
    lats.append(lat_data)
    hover_texts.append(title)
# print(mags[:10])
# print(lats[:5])
# print(longs[:5])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hover_texts,
    'marker': {
    'size': [4*mag for mag in mags],
    'color': mags,
    'colorscale': 'edge',
    'reversescale': True,
    'colorbar':{'title':'Magnitude'},
    },
}]

# data = [Scattergeo(lon=longs, lat=lats)]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')