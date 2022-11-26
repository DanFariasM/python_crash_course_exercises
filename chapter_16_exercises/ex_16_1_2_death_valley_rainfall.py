import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get precipitation data from this file.
    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        rain = float(row[3])
        dates.append(current_date)
        rainfall.append(rain)

# Plot the precipitation data.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c="blue")

# Format plot.
plt.title("Daily precipitation data - Death Valley - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("precipitation (in)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()