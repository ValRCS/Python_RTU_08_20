# def file_line_len(fpath):
#     with open(fpath, 'r', encoding='utf-8') as file:
#         lines = file.readlines() # loads all lines into a list - memory intensive
#     return len(lines)

def read_file_lines(file_path, encoding="utf-8"):
    '''Reads file and returns count of lines in file'''
    try:
        with open(file_path, "r", encoding=encoding) as veidenbaums:
            lines = veidenbaums.readlines()
            # the following will work even with large files
            line_count = 0
            for _ in lines :
                line_count += 1
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return 0
    return line_count # return once file is closed

src = "veidenbaums.txt"
print(f"File {src} has {read_file_lines(src)} lines")

src = "data/veidenbaums.txt"
print(f"File {src} has {read_file_lines(src)} lines")

def get_poem_lines(fpath, encoding='utf-8'):
    poem_lines = []
    with open(fpath, 'r', encoding=encoding) as file:
        # lines = file.readlines() # not needed
        for line in file:
            line = line.strip() # remove leading and trailing whitespace
            # so if we have non-empty line and it does not end with "***"
            if line and not line.endswith("***"):
                poem_lines.append(line)
    return poem_lines

poem_lines = get_poem_lines(src)
print(f"File {src} has {len(poem_lines)} poem lines")

def save_lines(destpath, lines, encoding='utf-8',end='\n'):
    with open(destpath, 'w', encoding=encoding) as file:
        for line in lines:
            file.write(line + end)
        # alternative with join
        # file.write(end.join(lines))
        # difference is that join will not add end to last line
        # possibly also a bit faster because we only do one write

dest = "data/veidenbaums_poem.txt"
save_lines(dest, poem_lines)

import string

def clean_punkts(srcpath,
                 destpath, 
                 bad_chars=string.punctuation, 
                 encoding='utf-8'):
    with open(srcpath,"r", encoding=encoding) as file:
        text = file.read()
        # new_text = ""
        # for char in text:
        #     if char not in str.punctuation:
        #         new_text += char
    for char in bad_chars:
        text = text.replace(char, "")
    with open(destpath, "w", encoding=encoding) as file2:
        file2.write(text)

src = "data/veidenbaums_poem.txt"
dest = "data/veidenbaums_poem_clean.txt"
# clean_punkts(src, dest) # turns out we also ned to exclude …
# so we need to add … to bad_chars
clean_punkts(src, dest, bad_chars=string.punctuation + "…")

from collections import Counter # should be at the top of the file
 
def get_word_usage(srcpath, destpath, lowercase=True, encoding='utf-8'):
    with open(srcpath, 'r', encoding=encoding) as file:
        text = file.read()
    if lowercase: # for normalization
        text = text.lower()
    words = text.split() # splits by any whitespace
    word_count = Counter(words)
 
    # hand written csv - will not work with words that have commas - but we cleaned those
    # with open(destpath, 'w', encoding=encoding) as file:
    #     # header
    #     file.write("Word, Count\n")
    #     for word, count in word_count.most_common():
    #         file.write(f"{word},{count}\n")
    # let's use csv module instead
    # this will let us easily handle words with commas
    # also we can specify encoding
    import csv
    with open(destpath, 'w', encoding=encoding) as file:
        writer = csv.writer(file, lineterminator='\n')
        # default lineterminator is \r\n which is Windows style
        # we get two newlines in the file which is not what we want
        writer.writerow(["Word", "Count"])
        # we go through tuples of (word, count) in order of most common
        for word, count in word_count.most_common():
            writer.writerow([word, count])

    # another alternative is to use pandas - more options for formatting

src = "data/veidenbaums_poem_clean.txt"
dest = "data/veidenbaums_poem_word_count.csv"
get_word_usage(src, dest)
