from pathlib import Path
import string
# 1a
def file_line_len(fpath):
    line_len = 0
    filepath = Path(fpath)
    if filepath.is_file():
        with open(filepath, encoding="utf-8") as f:
            # line_len = len(f.readlines()) # downside loads into memory for a moment, so not good for huge files
            line_len = sum(1 for line in f) # this will not need to load everything just 1s into memory for each line, so less memory
    else:
        print("No such file",  filepath, filepath.name, filepath.stem)
        line_len = -1
    return line_len
print(file_line_len("veidenbaums.txt"))
print(file_line_len("../LICENSE"))
print(file_line_len("../dirty_laundry.txt"))

"""
1b -> uzrakstam funkciju get_poem_lines(fpath), kas atgriež list ar tikai tām rindiņām kurās ir dzeja.
Tātad mums nederēs rindiņas bez teksta un nederēs dzejoļu virksraksti.
PS vēlams izmantot encoding = "utf-8"a
"""
def get_poem_lines(fpath):
    filepath = Path(fpath)
    verses_only = []
    if filepath.is_file():
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                # if 0<len(line.rstrip("\n")) and '***' not in line:
                if 0<len(line.strip()) and '***' not in line: # clean all whitespace and newlines
                    verses_only.append(line)
        return verses_only
    else:
        print('Invalid file')
        return []

print(len(get_poem_lines("veidenbaums.txt")))


def save_lines(destpath, lines, end="", encoding="utf-8"):
    filepath = Path(destpath)
    with open(filepath, mode="w", encoding=encoding) as f:
        f.writelines([line+end for line in lines])

save_lines("veid_clean_s21.txt", get_poem_lines("veidenbaums.txt"))

def clean_punkts(srcpath,destpath, badchars=string.punctuation,  encoding="utf-8",):
    # suiable for large files, for huge files you would want chunk
    with open(srcpath, encoding=encoding) as fin, open(destpath, mode="w", encoding=encoding) as fout:
        for line in fin:
            for c in badchars: # clean all bad chars
                line = line.replace(c,"")
            fout.write(line)

badchars = string.punctuation+"…"
print("Cleaning", badchars)
clean_punkts("veid_clean_s21.txt", "veid_clean_s21_no_punct.txt", badchars=badchars)

from collections import Counter
def get_word_usage(srcpath, destpath=""):
    with open(srcpath,encoding="utf-8") as f:
        txt = f.read()
    txt = txt.replace("\n", " ")
    tokens = txt.split(" ") # words basically
    count = Counter(tokens)
    print(count.most_common(50))
    with open(destpath, mode="w", encoding="utf-8") as f:
        f.write(str(count.most_common()))
    return count

get_word_usage("veid_clean_s21_no_punct.txt", "veid_counter_s21.txt")
# print(my_count.most_common(50))