# jekaterina
import collections
text = list(input("input dict:"))
c = collections.Counter(text)
print(c.most_common(5))
