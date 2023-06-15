# we have various built in methods for strings

# let's check for existence of a substring

haystack = "kartupelis"
print("kart" in haystack)
print("kart" not in haystack)

needle = "kart"
if needle in haystack:
    print(f"Found {needle} in {haystack}")
else:
    print(f"Did not find {needle} in {haystack}")


