# importing necessary libraries
from matplotlib import pyplot as plt
import numpy as np
# Line plot with different markers and line styles
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.figure(1)
plt.plot(x, y, marker='D', linestyle='--', color='r')
plt.plot(y, x, marker='o', linestyle='-.', color='c')
plt.plot(x, np.sin(x), linestyle="-.")
plt.figure(1)
# Bar, Scatter, and Histogram plots
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 10]
plt.figure(2)
plt.bar(categories, values, color='m', width=0.2)
plt.scatter(categories, values, color='g')
plt.hist(values, color='b', bins=5)
plt.title("Category Values")
plt.xlabel("Categories")
plt.ylabel("Values")
# Pie Chart and customizations
sizes = [50, 25, 25]
labels = ['Product A', 'Product B', 'Product C']
colors = ['gold', 'lightblue', 'lightgreen']
explode = (0.1, 0, 0)

plt.figure(3)
# Creating a pie chart
plt.pie(sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        shadow=True)
plt.title("Product Distribution")
# Saving the pie chart as an image file
plt.savefig("my_pie_chart.png")
print("Pie chart saved as 'my_pie_chart.png'")
plt.show()
