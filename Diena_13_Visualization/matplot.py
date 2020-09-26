import matplotlib.pyplot as plt
from PIL import Image

print("Making some images")
fig = plt.figure()

x = list(range(10))
y = [n**2 for n in x]
plt.bar(x, y)

plt.show()
