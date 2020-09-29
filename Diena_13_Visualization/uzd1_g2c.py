import random as ran
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

l = []


def dice_sum():
    num_start = 1
    num_end = 7
    num_total = 100_000
    for _ in range(0, num_total):
        num1 = ran.randrange(num_start, num_end)
        num2 = ran.randrange(num_start, num_end)
        num3 = ran.randrange(num_start, num_end)
        num4 = ran.randrange(num_start, num_end)
        num5 = ran.randrange(num_start, num_end)
        num6 = ran.randrange(num_start, num_end)
        l.append(num1+num2+num3+num4+num5+num6)
    return l


def pie_chart(data_list):
    data_list = data_list
    cnt = Counter(data_list)
    # print(cnt)
    dist_keys = Counter(data_list).keys()

    labels = []
    sizes = []

    for num in dist_keys:
        labels.append(num)
        sizes.append(cnt[num])

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
    ax1.axis('equal')
    plt.show()


def main():
    dice_sum()
    pie_chart(l)


if __name__ == "__main__":
    main()
