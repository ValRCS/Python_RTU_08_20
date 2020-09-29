fname = "missing_number.txt"
with open(fname) as f:
    lines = [int(n) for n in f]
print(sum(lines))
print(50*51/2 - sum(lines))
