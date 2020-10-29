def get_char_count(text):
    sdict = {}
    for n in text:
        # keys = sdict.keys()
        # if n in keys:
        #     sdict[n] += 1
        # else:
        #     sdict[n] = 1
        sdict[n] = sdict.get(n, 0) + 1 # so if no key return 0 add 1 and save
    return sdict
    
print(get_char_count('hubba bubba'))



# def get_char_count(myText):
#     myDict = {}
#     for x in myText:
#         myDict[x] = myText.count(x)
#     return myDict

print(get_char_count("hubba bubba"))