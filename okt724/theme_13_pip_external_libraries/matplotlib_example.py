# matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
# official page: https://matplotlib.org/
# Documentation: https://matplotlib.org/stable/contents.html
import matplotlib.pyplot as plt

# let's create a simple line plot using matplotlib
# we will create two lists x and y
# x will contain the x-axis values
# y will contain the y-axis values
# we will plot y = x^2
# we use list comprehension to create x and y
# x = [i for i in range(10)] # so x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = [i**2 for i in x] # so y = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# of course we can also use a for loop to create x and y
x = list(range(10)) # again x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = []
for i in x:
    y.append(i**2)

# now let's plot x and y
plt.plot(x, y)
# save as png
# ask if you want to save the plot as a file
# user_input = input("Do you want to save the plot as a file? (yes/no): ")
# if user_input.lower() == "yes":
#     plt.savefig("line_plot.png")
#     print("Plot saved as line_plot.png")
plt.show() # opens interactive window with the plot


