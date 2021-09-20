from pathlib import Path
import string

def file_line_len(fpath):
    # with open(fpath, encoding="utf-8") as f:
    #     return len(f.readlines()) # it is unclear if file will be properly closed
    # for bigger files that do not fit into mermory use the following:
    count = 0
    with open(fpath, encoding="utf-8") as f:
        for _ in f: #instead of line we use _ to signify that it is not needed
            count += 1
    return count

fname = Path("Veidenbaums.txt") # not strictly necesary but safer for longer file names 
print(file_line_len("veidenbaums.txt"))
print(file_line_len(fname))

badchars = "***"
def get_poem_lines(fpath, encoding="utf-8"):
    # clean_lines = []
    with open(fpath, encoding=encoding) as f:
        # below could also be written as list comprehension
        # for line in f:
        #     if len(line.strip()) > 0 and not badchars in line:
        #         clean_lines.append(line)
        clean_lines = [line for line in f if len(line.strip()) > 0 and not badchars in line]
    return clean_lines

poem_lines = get_poem_lines(fname)
print(poem_lines[:20])

dest = "veid_clean.txt"
def save_lines(destpath, lines, encoding="utf-8"):
    with open(destpath, mode="w", encoding="utf-8") as f:
        f.writelines(lines)

save_lines(dest, poem_lines)

dest_no_punct = "veid_no_punkt.txt"
def clean_punkts(srcpath,destpath, badchars=string.punctuation,  encoding="utf-8",):
    # suiable for large files, for huge files you would want chunk
    with open(srcpath, encoding=encoding) as fin, open(destpath, mode="w", encoding=encoding) as fout:
        for line in fin:
            for c in badchars: # clean all bad chars
                line = line.replace(c,"")
            fout.write(line)

clean_punkts(dest, dest_no_punct)

from collections import Counter
def get_word_usage(srcpath, destpath=""):
    with open(srcpath,encoding="utf-8") as f:
        txt = f.read()
    txt = txt.replace("\n", " ")
    tokens = txt.split(" ")
    count = Counter(tokens)
    return count # TODO save

my_count = get_word_usage(dest_no_punct)
print(my_count.most_common(50))