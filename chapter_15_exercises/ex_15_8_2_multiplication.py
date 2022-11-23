from plotly.graph_objs import Bar, Layout
from plotly import offline

from ex_15_8_1_die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls and store the results in a list.
results = []

for roll_num in range(5000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analize the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(title="Result of multiplying two D6 dice 5000 times",
            xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="dice_mult.html")