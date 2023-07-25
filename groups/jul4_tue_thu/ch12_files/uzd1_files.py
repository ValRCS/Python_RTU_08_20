# from string import punctuation
from re import sub
from collections import Counter
import string
 
# 1.
def file_line_len(fpath:str, encoding='utf-8') -> int:
    """
    fpath - filepath and filename with extension
    """
    with open(fpath, encoding=encoding) as f:
        line_cnt = len(f.readlines()) # will not work for large files
    return line_cnt  

def large_file_len(fpath:str, encoding='utf-8') -> int:
    """
    fpath - filepath and filename with extension
    works with large files as long as single line fits into memory
    """
    line_cnt = 0
    with open(fpath, encoding=encoding) as f:
        for _ in f: # we do not need the line itself
            line_cnt += 1
    return line_cnt

print(file_line_len('data/veidenbaums.txt'))
print(large_file_len('data/veidenbaums.txt'))

# 1b -> uzrakstam funkciju get_poem_lines(fpath), kas atgriež list ar tikai tām rindiņām kurās ir dzeja.
# Tātad mums nederēs rindiņas bez teksta un nederēs dzejoļu virksraksti.
# PS vēlams izmantot encoding = "utf-8"a
def get_poem_lines(fpath:str, encoding='utf-8') -> list:
    with open(fpath, "r", encoding=encoding) as file:
        lines = file.readlines()
    poem_rindas = [line.strip() for line in lines if line.strip() and not "***" in line]
    return poem_rindas

# 1c -> uzrakstam funkciju save_lines(destpath, lines)
# Šī funkcija noglabās destpath faila ceļā(tātad fails vai fails ar ceļu), visas lines
def save_lines(destpath, lines, encoding='utf-8', end="\n"):
    with open(destpath, mode="w", encoding=encoding) as file:
        for line in lines:
            file.write(line + end)

poem_lines = get_poem_lines("data/veidenbaums.txt")
save_lines("data/veidenbaums_poem.txt", poem_lines)

# 1e -> uzrakstam funkciju clean_punkts(srcpath,destpath)
# funkcija atvērs srcpath failu, attīrīs to no https://docs.python.org/3/library/string.html#string.punctuation
# un saglabās destpath 
def clean_punkts(srcpath, destpath, encoding='utf-8', punctuation=string.punctuation):
    with open(srcpath, "r", encoding=encoding) as src_file:
        text = src_file.read()

    # this is great
    # cleaned_text = text.translate(str.maketrans("", "", punctuation))
    # we could have also done this with regular loop
    # a bit slower but more readable
    for bad_char in punctuation:
        text = text.replace(bad_char, "")
 
    with open(destpath, "w", encoding=encoding) as dest_file:
        dest_file.write(text)

print(str.maketrans("", "", string.punctuation))
# exclam
print(chr(33))

bad_chars = string.punctuation + "…"
clean_punkts("data/veidenbaums_poem.txt", 
             "data/veidenbaums_clean.txt", 
             punctuation=bad_chars)

# 1f -> uzrakstam funkciju get_word_usage(srcpath, destpath)
# funkcija atver failu un atrod biežāk lietotos vārdus
# ieteikums izmantot Counter moduli !
# uzskatīsim, ka vārdi tiek atdalīti vai nu ar whitespace vai newline (vecais labais split noderēs)
def get_word_usage(srcpath, destpath, encoding='utf-8', normalize=True):
    with open(srcpath, "r", encoding=encoding) as file:
        text = file.read()
    if normalize:
        # text = sub(r"\s+", " ", text) # this would replace all whitespace with single space
        # we dont really need it since split() will split on any whitespace anyways
        text = text.lower()

    words = text.split()
    word_counter = Counter(words)
    popular_words = word_counter.most_common() # returns list of tuples ordered by count descending
 
    # Saglabā rezultātus failā
    with open(destpath, "w", encoding=encoding) as dest_file:
        # write header
        dest_file.write("word,count\n")
        for word, count in popular_words:
            dest_file.write(f"{word},{count}\n")

get_word_usage("data/veidenbaums_clean.txt", "data/veidenbaums_word_usage.csv")

# let's make a function that reads csv and plots one column vs another

# 1g -> uzrakstam funkciju plot_csv(srcpath, x_col, y_col)

def plot_csv(srcpath, x_col="word", y_col="count", encoding='utf-8'):
    import matplotlib.pyplot as plt

    # let's use csv module to read csv this is standard library
    # in real life i would use pandas
    import csv
    with open(srcpath, "r", encoding=encoding) as file:
        reader = csv.DictReader(file)
        # we will use list comprehension to create list of dicts
        # we could have also used list(reader)
        data = [row for row in reader]
        # print keys
        print(data[0].keys())
    

    # X = data[0][x_col]
    X = [row[x_col] for row in data]
    # Y = data[0][y_col]
    Y = [int(row[y_col]) for row in data]
    # top 50 words
    X = X[:50]
    Y = Y[:50]
    plt.bar(X, Y)
    
    # i could save the file
    plt.savefig("data/veidenbaums_word_usage.png")
    plt.show()

plot_csv("data/veidenbaums_word_usage.csv")

# more info on matplotlib
# tutorial: https://matplotlib.org/tutorials/introductory/pyplot.html