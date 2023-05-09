# 1e -> uzrakstam funkciju clean_punkts(srcpath,destpath)
# funkcija atvērs srcpath failu, attīrīs to no https://docs.python.org/3/library/string.html#string.punctuation
from string import punctuation
def clean_punkts(srcpath,
                 destpath, 
                 encoding="utf-8", 
                 punct=punctuation, 
                 replace_with=""):
    with open(srcpath, encoding=encoding) as file:
        text = file.read()
    # so one character at a time we replace it with ""
    for bad_char in punct:
        text = text.replace(bad_char, replace_with)
    # save into destpath
    with open(destpath, mode="w", encoding=encoding) as file:
        file.write(text)

# clean_punkts("veidenbaums_poems.txt", "veidenbaums_clean_may2.txt")
my_punct = punctuation+"…"
clean_punkts("veidenbaums_poems.txt", "veidenbaums_clean_may2.txt", punct=my_punct)
clean_punkts("veidenbaums_poems.txt", "veidenbaums_clean_may2_smiley.txt", replace_with="😀")