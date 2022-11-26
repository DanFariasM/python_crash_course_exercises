import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_weather_data(filename):
    """Get the high and low temperature data from the file."""

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get indexes from the csv file.
        date_index = header_row.index("DATE")
        high_index = header_row.index("TMAX")
        low_index = header_row.index("TMIN")

        # Get dates and high and low temperatures from this file.
        for row in reader:
            current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


def plot_temperatures(line_transparency, fill_stranparency):
    """Plot the high and low temperatures."""
    ax.plot(dates, highs, c="red", alpha=line_transparency)
    ax.plot(dates, lows, c="blue", alpha=line_transparency)
    plt.fill_between(dates, highs, lows, facecolor="blue",
                    alpha=fill_stranparency)

plt.style.use("seaborn")
fig, ax = plt.subplots()

# Get Sitka information and plot it.
filename = "data/sitka_weather_2018_simple.csv"
dates, highs, lows = [], [], []
get_weather_data(filename)
plot_temperatures(0.6, 0.15)

# Get Death Vallet information and plot it.
filename = "data/death_valley_2018_simple.csv"
dates, highs, lows = [], [], []
get_weather_data(filename)
plot_temperatures(0.3, 0.05)

# Format plot.
title = "Daily high and low temperatures - 2018\nSitka and Death Valley"
plt.title(title, fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

ax.axis([dates[0], dates[-1], 0, 150])

plt.show()