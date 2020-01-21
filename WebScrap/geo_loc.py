import pandas as pd
import matplotlib.pyplot as plt
from bbox import BBox2D
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
cols = ['id', 'user_id', 'lat', 'lon', 'recorded_time', 'created_at', 'updated_at']
df = pd.read_csv('/home/ramesh/Downloads/user_locations.csv', names=cols)
print(df.dtypes.index)
lat = df.lat.tolist()
lon = df.lon.tolist()
np_arr = np.array(df[['lon','lat']])
print(np_arr.shape)
clustering = DBSCAN(eps=0.001, min_samples=6).fit(np_arr)
labels = clustering.labels_
print(np.unique(labels))
l = list(labels)
print(l.count(6))
# plt.scatter(np_arr[:,0], np_arr[:, 1], c=labels)
# plt.show()
import gmplot

colors=['red','blue','green','purple','black', 'brown','yellow']
gmap3 = gmplot.GoogleMapPlotter(27.6853391, 85.3199828, 13)
for i in range(len(lat)):
    gmap3.scatter([lat[i]],[lon[i]], colors[labels[i]], size=10, marker=False)


# heatmap plot heating Type
# points on the Google map
# gmap4.heatmap(lat, lon)
#
gmap3.draw("C:\\Users\\user\\Desktop\\map14.html")
# Plot method Draw a line in
# between given coordinates
# gmap3.plot(lat, lon,
#            'cornflowerblue', edge_width=2.5)
#
# gmap3.draw("C:\\Users\\user\\Desktop\\map13.html")
# print(np.concatenate((np.array(lat), np.array(lon)), axis=0))
# fig = go.Figure(data=go.Scattergeo(
#         lon = df['lon'],
#         lat = df['lat'],
#         # text = df['text'],
#         mode = 'markers',
#         # marker_color = df['cnt'],
#         ))
#
# fig.update_layout(
#         title = 'Nepal GeoPoints',
#         geo_scope='asia',
#     )
# fig.show()