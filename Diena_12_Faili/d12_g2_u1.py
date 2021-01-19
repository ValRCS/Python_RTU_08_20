# def file_line_len(fpath):
#     """ Return number of lines in fpath file"""
#     my_lines = open(fpath, encoding="utf-8").readlines() # with big files this might not work
#     return len(my_lines)
import string
from collections import Counter

def file_line_len(fpath):
    with open(fpath, encoding="utf-8") as f:  # create a file object
        num_lines = sum(1 for line in f)
        print(f'Found {num_lines} lines in file: {fpath}')
    return num_lines

def get_poem_lines(fpath):
    with open(fpath, encoding="utf-8") as f:  # create a file object
        filtered_lines = [line for line in f if line[0] != "\n" and not line[-4:] == "***\n"]
        num_lines = len(filtered_lines)
        print(f'Found {num_lines} poem lines in file: {fpath}')
    return filtered_lines
 
#1c uzdevums
def save_lines(destpath, lines):
    with open(destpath, mode="w", encoding="utf-8") as fout:
        fout.writelines(lines)
        # for line in lines:
        #     fout.write(line)

#1e
def clean_punctuation(srcPath, destPath, punct = string.punctuation):
    with open(srcPath, encoding='utf-8') as readFile, open(destPath, mode='w', encoding='utf-8') as writeFile:
        fileContent = readFile.read() # for huge files we'd have to go line by line
        for symbol in punct:
            fileContent = fileContent.replace(symbol, "")
        writeFile.write(fileContent)

#1F
def get_word_usage(srcpath, destpath):
    """Count words from srcpath and save the list of counted words in destpath"""
    with open(srcpath, encoding="utf-8") as f, open(destpath, "w", encoding="utf-8") as dest:
        word_count = Counter(word.lower() for line in f for word in line.split())
        # dest.write(str(word_count))
        # CSV gen by hand
        dest.writelines([str(row[0])+","+str(row[1])+"\n" for row  in word_count.most_common()])

print(file_line_len("veidenbaums.txt"))
lines = get_poem_lines("veidenbaums.txt")
save_lines("veidenbaums_clean.txt", lines)

clean_punctuation("veidenbaums_clean.txt", "veid_no_punct.txt")
get_word_usage("veid_no_punct.txt", "veid_common.csv")





