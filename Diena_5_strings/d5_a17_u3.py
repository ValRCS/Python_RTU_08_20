#3rd task:
words=input("Tell me something that is not bad! ")
i=words.find("not ")
k=words.find("no ")
l=words.find("Not ")
m=words.find("No ")
j=words.find("bad") #also need to consider other possibilities like "badly" etc, otherwise it gives "goodly", but if I will use "bad " #program will ignore "bad," and "bad." 
if "not " in words and i<j:
    x=words[i:j+3]
    replace=words.replace(x, "good")
    print(replace)
elif "no " in words and k<j:
    x=words[k:j+3]
    replace=words.replace(x, "good")
    print(replace)
elif "Not " in words and l<j:
    x=words[l:j+3]
    replace=words.replace(x, "Good")
    print(replace)
elif "No " in words and m<j:
    x=words[m:j+3]
    replace=words.replace(x, "Good")
    print(replace)
else:
    print(words)