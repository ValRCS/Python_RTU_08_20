import string
from collections import Counter

def file_line_len(fpath) :
    with open(fpath, encoding = "UTF-8") as vv:
        # print(sum(1 for n in vv))
        line_len = len(vv.readlines()) # for huge files it might be better to count each line but not read
    return line_len
# print(file_line_len("../data/veidenbaums.txt"))
# print(file_line_len("frost.txt"))

def get_poem_lines(fpath):
    with open(fpath, encoding="utf-8") as f:
        poem_lines = []
        for line in f:
            if len(line.strip()) !=0 and not line.rstrip().endswith("***"):
                poem_lines.append(line)
    return poem_lines

# print(get_poem_lines("../data/veidenbaums.txt")[:10])

def save_lines(destpath, lines, encoding="utf-8"):
    with open(destpath, 'w', encoding=encoding) as f:
        f.writelines(lines)
        # for line in lines:
        #     f.write(line)

# save_lines("v_filt.txt", get_poem_lines("../data/veidenbaums.txt")[:10])
# save_lines("v_filt_20.txt", get_poem_lines("../data/veidenbaums.txt")[:20])

#1e
def clean_punctuation(srcPath, destPath, punct = string.punctuation):
    with open(srcPath, encoding='utf-8') as readFile, open(destPath, mode='w', encoding='utf-8') as writeFile:
        fileContent = readFile.read()
        for symbol in punct:
            fileContent = fileContent.replace(symbol, "")
        writeFile.write(fileContent)

def get_word_usage(fpath, destpath, count = None):
    with open(fpath, encoding='utf-8') as f:
        most_commons = Counter(word for line in f for word in line.split()).most_common(count)
    with open(destpath, 'w', encoding='utf-8') as f:
        f.write(str(most_commons))   

if __name__ == "__main__":

    save_lines("v_filt_all.txt", get_poem_lines("../data/veidenbaums.txt"))
    clean_punctuation("v_filt_all.txt", "v_cleaned.txt")
    get_word_usage("v_cleaned.txt","v_count.txt")