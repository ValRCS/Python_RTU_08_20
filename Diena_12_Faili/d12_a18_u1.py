import string
from collections import Counter
 
# 1a
def file_line_len(fpath):
    with open(fpath, encoding = "utf-8") as f_v:
        lines_count = len(f_v.readlines()) # so all the lines will be in memory
        # for truly large files the following will work better
        # lines_count=0
        # for _ in f_v:
        #     lines_count += 1
    return lines_count

path = "veidenbaums.txt"

print(file_line_len(path))

# 1b
def get_poem_lines(fpath):
    with open(fpath, encoding='utf-8') as f:
        poem_lines = []
        for line in f:
            if len(line.strip()) !=0 and not line.rstrip().endswith('***'):
                poem_lines.append(line.rstrip('\n'))
    return poem_lines
# print(get_poem_lines(path))

# 1c
def save_lines(destpath, lines, encoding='utf-8', end="\n"):
    with open(destpath, 'w', encoding=encoding) as f:
        for line in lines:
            f.write(line+end)
        # f.write(end.join(lines)) # so last line will not have end


save_lines("veid_poem_o27.txt", get_poem_lines(path))


# 1e
def clean_punkts(srcpath,destpath,bad_chars=string.punctuation):
    with open(srcpath, encoding='utf-8') as f_in, open(destpath, mode='w', encoding='utf-8') as f_out:
        file_str = f_in.read()
        for char in bad_chars:
            file_str=file_str.replace(char,"")
        f_out.write(file_str)

print("Cleaning file from", string.punctuation)
clean_punkts("veid_poem_o27.txt","veid_no_punct_o27.txt", bad_chars=string.punctuation+"…")


def get_word_usage(srcpath, destpath):
 
    my_words = ""
    with open(srcpath, encoding="utf-8") as f:
        for line in f:
            my_words += " " + line.rstrip("\n")  # for large files this will not be fastest
 
    my_words = my_words.strip().lower()
    while "  " in my_words:
        my_words = my_words.replace('  ', ' ')
 
    my_words = my_words.split()
 
    cnt = Counter(my_words)
    # for word in my_words:
    #     cnt[word] += 1
 
    print(cnt)
    
    # marklist = sorted(cnt.items(), key = lambda x:x[1], reverse = True)
    # cnt = dict(marklist)
    print(cnt.most_common(10))  #top lilst
 
    with open(destpath, mode = "w", encoding="utf-8") as f:
        # for key, value in cnt.items():
        for key, value in cnt.most_common():
            my_s = f"{key} {value}"
            f.write(f"{my_s}\n")

get_word_usage("veid_no_punct_o27.txt", "veid_stats_o27.txt")