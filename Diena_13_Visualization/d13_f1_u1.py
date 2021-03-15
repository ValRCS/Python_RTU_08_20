import random
import collections
import matplotlib.pyplot as plt
 
def roll_dice():
    random_roll = []
    for i in range(1,7):
        random_roll.append(random.randint(1, 6))
    return random_roll
 
def roll_sum(times):
    six_dice_sum = []
    for i in range(1,times+1):
        six_dice_sum.append(sum(roll_dice()))
    return six_dice_sum
 
all_sums = roll_sum(100000)
frequency_of_sums = collections.Counter(all_sums)
 
plt.bar(frequency_of_sums.keys(), frequency_of_sums.values())
plt.ylabel('Frequency')
plt.title('6 Dice roll sum histogram')
 
plt.show()