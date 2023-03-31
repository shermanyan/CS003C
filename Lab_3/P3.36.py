from matplotlib import pyplot

# Add the labels of all the areas of all continents
labels = ['Asia', 'Africa', 'North America', 'South America', 'Antarctica', 'Europe', 'Australia']

# Assign the sizes for corresponding continents
sizes = [44.6, 30.1, 24.2, 17.8, 13.2, 9.9, 8.1]

# Assign the colors for corresponding continents
colors = ['red', 'brown', 'blue', 'green', 'white', 'orange', 'tan']

# Explode the second slice of pie chart
explode = (0, 0.1, 0, 0, 0, 0, 0)

# Draw the piechart using pie() command
pyplot.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

# Set aspect ratio to be equal to draw the pie as circle
pyplot.axis('equal')

# Add the description to the chart
pyplot.legend(labels, loc=6, fontsize=9)

# Display the chart
pyplot.show()
