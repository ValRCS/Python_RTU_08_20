from pathlib import Path
from collections import Counter
from string import punctuation

# Ex 1a
def file_line_len(fpath):
    with open(fpath, encoding="utf-8") as poems:
        i=0
        for _ in poems:
            i+=1
    return i

# 1a return number of lines in file
# this will take memory on huge file, so above solutions is preferred
# def file_line_len(fpath):
#     with open(fpath, encoding='utf-8') as fin:
#         line_count = len(fin.readlines())
#     return line_count

print(file_line_len("veidenbaums.txt"))

### Task 1b
 
# def get_poem_lines(fpath):
#     my_text = ""
#     with open(fpath, mode="r", encoding="utf-8") as my_file:
#         for line in my_file:
#             if "***" not in line:
#                 if not line.isspace():
#                     print(line.replace("\n", ""))
#                     my_text += line # text buffer will not be efficient for large texts
#     return my_text

# 12.B
def get_poem_lines(fpath):
  with open (fpath, encoding = "utf-8") as f:
    # poem=[]
    # for row in f:
    #   if not(row=="\n" or "***" in row):
    #     poem.append(row.rstrip("\n"))
    #     # poem.append(row.rstrip("\n"))
    poem = [row for row in f if not(row=="\n" or row.endswith("***\n"))]	
  return poem

poem_lines = get_poem_lines("veidenbaums.txt")
print(poem_lines[:200])

# 12.C
def save_lines(destpath, lines, end=""):
  with open (destpath, "w", encoding = "utf-8") as f:
    for x in lines:
      f.write(x+end)

save_lines("veidenbaums_poem.txt", poem_lines)

# 1e remove punctuation
def clean_punkts(srcpath, destpath, punctuation=punctuation):
    trans_table = ''.maketrans({ord(c): None for c in punctuation})
    with open(srcpath, encoding='utf-8') as fin, open(destpath, mode="w", encoding='utf-8') as fout:
        for line in fin:
            for c in punctuation:
                line = line.replace(c, "")
            fout.write(line)
            # same as above innner loop but using translate
            # fout.write(line.translate(trans_table))

print(punctuation)

clean_punkts("veidenbaums_poem.txt", "veidenbaums_no_punkt.txt", punctuation=punctuation+"…")

# 1f get word usage
def get_word_usage(srcpath, destpath):
    # with open(srcpath, encoding='utf-8') as fin:
    #     result = fin.readlines()
    # trans_table = ''.maketrans({ord(c): None for c in punctuation})
    with open(srcpath, encoding='utf-8') as fin:
        full_text = fin.read().lower()
    count = Counter(full_text.split())

    with open(destpath, mode="w", encoding='utf-8') as fout:
        for index, (key, value) in enumerate(count.most_common(), start=1):
            fout.write(key + ', ' + str(value) + '\n')
            if index < 11:
                print(f'{index}.: "{key}" x {value}')


get_word_usage("veidenbaums_no_punkt.txt", "veidenbaums_word_usage.txt")