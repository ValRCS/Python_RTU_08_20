# 1a uzdevums

# essentially we implement wc -l command line utility from linux
# def file_line_len(fpath):
#     with open(fpath, mode="r", encoding="utf-8") as f:
#         text = f.readlines() # this reads whole file into a list
#     return len(text)

# for larger file sizes, we can use another approach

import string
from pathlib import Path
from collections import Counter

data_path = Path("data")

def file_len(filename):
    count = 0
    with open(filename, encoding="utf-8") as r:
        # for count, _ in enumerate(r): # _ means that we don't care about the value
        #     pass
        for _ in r: # so we loop rows, but we don't care about the value
            count += 1 # simple counter
    print(f"The counting of number of total lines is: {count }")
    return count 
 
print(file_len("data/veidenbaums.txt"))

def get_poem_lines(filename, encoding="utf-8"):
    new_text = []
    with open(filename, encoding=encoding) as r:
        text = r.readlines()
        for line in text:
            # so if line has anything after stripping whitespace
            #  and it doesn't end with "***"
            if line.strip() and not line.rstrip().endswith("***"):
                new_text.append(line)
    return new_text

clean_text = get_poem_lines("data/veidenbaums.txt")
# print first 10 lines
print(*clean_text[:10], sep="") # unroll list slice 

# 1c
def save_lines(destpath, lines, encoding="utf-8"):
    with open(destpath, "w", encoding=encoding) as f:
        f.writelines(lines)

# save_lines("data/veidenbaums_clean.txt", clean_text)
# we could have done this in one line
save_lines("data/veidenbaums_clean.txt", get_poem_lines("data/veidenbaums.txt"))

def clean_punkts(srcpath, destpath, bad_chars=string.punctuation, encoding="utf-8"):
    with open(srcpath, encoding=encoding) as f:
        lines = f.readlines()
        #remove punctuation
        lines = [l.translate(str.maketrans("", "", bad_chars)) for l in lines]
    # better to save afterwards in case we use same file for src and dest
    # here srcpath is already closed
    save_lines(destpath, lines, encoding=encoding)

clean_punkts(data_path / "veidenbaums_clean.txt", data_path / "veidenbaums_no_punkts.txt")
# so if we also want to clean … then we simply add it to the bad_chars

clean_file = data_path / "veidenbaums_clean.txt"
no_punkts_file = data_path / "veidenbaums_no_punkts.txt"
bad_chars = string.punctuation+"…"
print(f"Cleanning {clean_file} from punctuation and {bad_chars}")
print(f"Saving to {no_punkts_file}")	
clean_punkts(clean_file, no_punkts_file, bad_chars=bad_chars)

def get_word_usage(srcpath, destpath):
    with open(srcpath, encoding="utf-8") as f:
        lines = f.readlines()
        #split lines into words and lowercase
        words = [w.lower() for l in lines for w in l.split()]
        #count words
        word_counts = Counter(words)
        #sort by count
        # sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        # get most common as list of tuples
        sorted_word_counts = word_counts.most_common()# by default all items
        #save to file
        with open(destpath, "w", encoding="utf-8") as f:
            # let's write a header
            f.write(f"{'Word':<20}\t{'Count':<10}\n")
            # so we are unpacking tuples into word and count
            # this will be tsv file - tab separated values
            f.writelines([f"{word}\t{count}\n" for word, count in sorted_word_counts])

get_word_usage(no_punkts_file, data_path / "veidenbaums_word_usage.tsv")


