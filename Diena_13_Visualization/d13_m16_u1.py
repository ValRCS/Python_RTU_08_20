# 1.uzd
 
import random
from collections import Counter
from matplotlib import pyplot as plt
# import pandas
# import plotly.graph_objs as go
 
 
def get_throw_list( sides = 6, throws = 100_000 ):
    throw_list = [sum(random.randint(1,6) for i in range(sides)) for n in range(throws)]
    return throw_list
 
c = Counter(get_throw_list())
 
plt.bar(c.keys(),c.values())
plt.show()