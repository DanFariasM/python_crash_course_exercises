import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/world_fires_1_day.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get latitudes, longitudes, brightness and dates from this file.
    lats, longs, brightnesses, dates = [], [], [], []
    hover_texts = []
    for row in reader:
        lats.append(row[0])
        longs.append(row[1])
        brightnesses.append(float(row[2]))
        date = datetime.strptime(row[5], '%Y-%m-%d')
        label = f"{date.strftime('%m/%d/%y')} - {float(row[2])}"

        hover_texts.append(label)


# Mapping the fires.
data = [{
    "type": "scattergeo",
    "lat": lats,
    "lon": longs,
    "text": hover_texts,
    "marker": {
        "color": brightnesses,
        "colorscale": "YlOrRd",
        "reversescale": True,
        "colorbar": {"title": "Brightness"},
    },
}]

my_layout = Layout(title="World Fires - Sep 22-23, 2018")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_fires.html")