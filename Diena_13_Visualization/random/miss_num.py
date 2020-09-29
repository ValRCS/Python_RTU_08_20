import random
nums = [str(n)+"\n" for n in range(1, 51)]
random.shuffle(nums)
print(nums)
nums.pop()
with open("missing_number.txt", "w") as f:
    f.writelines(nums)
