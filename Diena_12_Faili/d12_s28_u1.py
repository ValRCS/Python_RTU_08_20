import string
from collections import Counter

def file_line_len(fpath):
    with open(fpath, encoding="utf-8") as f:
        # count = 0
        # for _ in f: # _ - not used
        #     count += 1
        # same as above
        count = sum(1 for _ in f)  # crucially we are summing a generator not a list, so we no zillion 1s in memory
    return count  # f is closed here

print(file_line_len("veidenbaums.txt"))

# 1.b #
def get_poem_lines(fpath):
    with open(fpath, encoding = "utf-8") as f:
        # poem_lines = []
        # for line in f:
        #     # if len(line.strip()) !=0 and not line.rstrip().endswith("***"):
        #     if line.strip() and not line.rstrip().endswith("***"):
        #         poem_lines.append(line.rstrip("\n"))
        #         # print(poem_lines)
        # list comprehension same as above except we keep newlines
        poem_lines = [line for line in f if line.strip() and not line.rstrip().endswith("***")]
    return poem_lines

poem_lines = get_poem_lines("veidenbaums.txt")
print(len(poem_lines))

#1.c
dest_path = "veidenbaums_poems.txt"
def save_lines(destpath, lines, encoding="utf-8"):
    with open(destpath, mode="w", encoding=encoding) as f:  # i pass encoding along with mode
        f.writelines(lines)

#1.d
#1.d
save_lines(dest_path, poem_lines)

#1.e
dest_no_punct_path = "veidenbaums_no_punkts.txt"
print("Cleaning", string.punctuation)
def clean_punkts(srcpath,destpath, bad_chars=string.punctuation,  encoding="utf-8",):
    with open(srcpath, encoding=encoding) as fin, open(destpath, mode="w", encoding=encoding) as fout:
        for line in fin:
            for c in bad_chars: 
                line = line.replace(c,"")
            fout.write(line)
 
# clean_punkts(dest_path, dest_no_punct_path)
clean_punkts(dest_path, dest_no_punct_path, bad_chars=string.punctuation + "…")
# above will work if bad_chars is actually a list of bad words

# 1.f
def get_word_usage(srcpath, destpath= ""):
    with open(srcpath,encoding="utf-8") as f:
        text = f.read()
    text = text.replace("\n", " ")
    text = text.lower() # lowercase
    words = text.split(" ")
    counter = Counter(words)
    if destpath:
        with open(destpath, mode="w", encoding="utf-8") as f:
            for word, count in counter.most_common(): # most_common() is a list of tuples
                f.write(f"{word} {count}\n")
    return counter 

no__punct_count = get_word_usage(dest_no_punct_path, "veidenbaums_count.txt")
print(no__punct_count)