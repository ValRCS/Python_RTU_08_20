import string
import collections
from collections import Counter
 
# def file_line_len(fpath):
#     lines = len(open(f'{fpath}', encoding="utf-8", mode="r").readlines())
#     return lines
    
# for huuuge files where we do not want to read all the lines in memory
def file_line_len(fpath):
    cnt = 0
    with open(fpath, encoding="utf-8") as f:
        for _ in f: # we do not use line so can use _ to signify that its  not used
            cnt += 1
    return cnt

print(file_line_len("veidenbaums.txt"))

def get_poem_lines(fpath):
    lines = []
    with open(fpath, encoding="utf-8") as f:
        for line in f:
            if line[0] != "\n" and "***" not in line: # could use not line.endswith("***\n")
                lines.append(line)
    return lines

def save_lines(dest, lines):
    with open(dest, mode="w", encoding="utf-8") as f:
        f.writelines(lines)
        # for line in lines:
        #     f.write(line)

save_lines("veid_1103.txt", get_poem_lines("veidenbaums.txt"))

def clean_punkts(srcpath, destpath, punct = string.punctuation): # putting punct in arguments we can supply our own blacklist
    with open(srcpath, encoding= "utf-8") as readfile, open(destpath, mode="w", encoding= "utf-8") as writefile:
        punct_file = readfile.read()
        for char in punct:
            punct_file = punct_file.replace(char,"")      
        writefile.write(punct_file)

# clean_punkts("veid_1103.txt", "veid_1103_nopunkts.txt")
clean_punkts("veid_1103.txt", "veid_1103_nopunkts.txt", punct = string.punctuation+"…"  )


 
# def get_word_usage(srcpath, destpath):
#     c = collections.Counter
#     full_list = []
#     with open(f'{srcpath}', encoding="utf-8", mode="r") as fin, open(f'{destpath}', mode="w", encoding="utf-8") as fout:
#         for i in fin:
#             line = i.translate({ord(c): None for c in string.punctuation}).lower().rstrip('\n')
#             line_list = line.split(" ")
#             for n in line_list:
#                 full_list.append(n)
#         fout.write(f'{c(full_list)}')

def get_word_usage(srcpath, destpath):
    with open(srcpath, encoding="utf-8") as fin, open(destpath, mode="w", encoding="utf-8") as fout:
        lines = fin.read().lower()
        words = lines.split()
        c = Counter(words)
        fout.write("\n".join(str(i) for i in c.most_common()))
 
 
get_word_usage("veid_1103_nopunkts.txt", "tester2.txt")