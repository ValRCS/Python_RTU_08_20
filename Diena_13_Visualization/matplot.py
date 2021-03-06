import matplotlib.pyplot as plt  # very typical
# Mathplotlib library
# inspired by MATLAB
# https://matplotlib.org/3.3.2/contents.html
# https://realpython.com/python-matplotlib-guide/
# https://matplotlib.org/3.3.2/tutorials/index.html
# print("Making some images")
# fig = plt.figure()

x = list(range(11))
y = [n**2 for n in x]
y2 = [n+5 for n in y]
y3 = [n+15 for n in y]
# so I plot multiple plots on one graph
plt.bar(x, y)
plt.plot(x, y2)
plt.scatter(x, y3)
# there is also an option to plot separate graphs
plt.savefig("simplegraph.png") #jpg i think also gif formats are supported

plt.show() #this will open interactive window
