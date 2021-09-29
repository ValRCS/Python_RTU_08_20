# https://docs.python.org/3/library/functions.html#built-in-functions
my_results = [True, True, 2*2==4, True]
print(all(my_results)) # all statements in the sequence should be truthy to get True else we get False
my_results.append(False)
print(my_results)
print(all(my_results)) #In logic this is called universal quantor, all my)_results must be truthy for all to return True

print(any(my_results)) # any just needs one true result inside, existences kvantors, one or more items are true

print(len(my_results))
my_results.append(9000)
print("max", max(my_results)) # we only have 1 or 0 in my_results
my_results.append(-30)
print(my_results)
print("min", min(my_results))
print("summa", sum(my_results)) # well when summing booleans True is 1 and False is 0
# print(min(my_results))