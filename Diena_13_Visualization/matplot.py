import matplotlib.pyplot as plt  # very typical to rename to something shorter
# Mathplotlib library
# inspired by MATLAB
# https://matplotlib.org/3.3.2/contents.html
# https://realpython.com/python-matplotlib-guide/
# https://matplotlib.org/3.3.2/tutorials/index.html
print("Making some images")
fig = plt.figure()

x = list(range(11))  # 0 to 10
y = [n**2 for n in x]  # square of x
y2 = [n+5 for n in y] # add 5 to y
y3 = [n+15 for n in y] # add 15 to y
# so I plot multiple plots on one graph

# # we pass x as a list and y as a list
# plt.bar(x, y) # bar chart
plt.plot(x, y, 'r', label='y')  # r stands for red
plt.plot(x, y2) # line chart
plt.scatter(x, y3) # scatter plot
# # there is also an option to plot separate graphs
# it will save image in current working directory
plt.savefig("bildeJun27.png") #jpg i think also gif formats are supported

plt.show() #this will open interactive window
