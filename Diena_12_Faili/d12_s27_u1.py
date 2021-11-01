import os
import string
from pathlib import Path
 
def file_line_len(fpath):
    count = 0
    with open(fpath, encoding="utf-8") as f:
        for line in f:  # does not require reading all lines into memory at once
            count += 1
    return count

def get_poem_lines(fpath):
    with open(fpath, encoding="utf-8") as f:
        all_lines = [line.replace("\n", "") for line in f if len(line.strip()) > 0 if not "***" in line]
 
    return all_lines

source_file = "veidenbaums.txt"

# def save_lines(destpath, lines, prefix="just_lines", suffix="veidenbaums.txt"):
#     lines_file = prefix + "_" + suffix
#     print(lines_file)
#     with open(destpath, mode="w", encoding="utf-8") as f:

def save_lines(destpath, lines, end="\n"):
    with open(destpath, mode="w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + end)
        # could use f.write(end.join(lines)) # but no line breaks in the end
        # but then last line has no newline

# 1.d - with nice functions I can compose a mini file processing pipeline - conveyer
save_lines("veidenbaums_lines.txt", get_poem_lines(source_file))

# 1e
print(string.punctuation)

def clean_punkts(srcpath,destpath, bad_chars=string.punctuation):
    # bad_chars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    # bad_chars_list = list(bad_chars) # no need to convert to list, we can iterate a string
    with open(srcpath, encoding="utf-8") as inFile, open(destpath, "w", encoding="utf-8") as outFile:
        for line in inFile:
            # for ch in line:
            #     if ch not in bad_chars:  # if bad_chars were a set this could be a bit faster
            #         outFile.write(ch)  # writing each char to the file one by one
            #         # possibly might want to delay flushing to disk
            # same as above double loop
            for ch in bad_chars:
                line = line.replace(ch, "")
            outFile.write(line)
 
# clean_punkts("veidenbaums_lines.txt", "veidenbaums_no_punkts.txt",bad_chars=string.punctuation+"…")
clean_punkts("veidenbaums_lines.txt", "veidenbaums_no_kur_tik.txt",bad_chars=("Kur", "Tik"))