import string
print("Our punct:", string.punctuation)
def clean_punkts(srcpath,destpath, badchars = string.punctuation):
    with open(srcpath,mode="r", encoding="utf-8") as inf, open(destpath,mode="w", encoding="utf-8") as outf:
        # for line in inf:
        #     for char in badchars:
        #         line = line.replace(char,'')
        #     outf.write(line)
        text = inf.read() # could just proceses whole text at once
        for char in badchars:
            text = text.replace(char,'')
        outf.write(text)

# clean_punkts("veidenbaums_poems.txt","veidenbaums_no_punkts.txt")
clean_punkts("veidenbaums_poems.txt","veidenbaums_no_punkts.txt", badchars = string.punctuation + "…A")

