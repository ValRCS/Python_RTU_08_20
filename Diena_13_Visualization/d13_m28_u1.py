import random
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt 
 
# 1.
NUM_THROWS = 1_000_000 # _000 
DICE_PER_THROW = 2


def throw_dice(turns:int = 1):
    dice_result = []
    for _ in range(turns):
        rndm_num = random.randint(1,6)
        dice_result.append(rndm_num)
    return sum(dice_result)
 
big_dice_result = [throw_dice(DICE_PER_THROW) for _ in range(NUM_THROWS)]
top_sums = Counter(big_dice_result)
 
plt.bar(top_sums.keys(),top_sums.values()) # bar chart
plt.show()