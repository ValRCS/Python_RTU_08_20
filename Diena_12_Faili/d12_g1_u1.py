import os
import string
print(os.getcwd())
# 1a
# def file_line_len(fpath):
#     return len(open(fpath, mode="r", encoding="utf-8").readlines(  )) # could take too much memory on big files

def file_line_len(fpath):
    with open(fpath, encoding="utf-8") as f:  # create a file object
        count = 0
        for _ in f: 
            count +=1
    return count
print(file_line_len('veidenbaums.txt'))
 
# print(file_line_len("Diena_12_Faili/frost.txt"))   #971
# print(file_line_len("Diena_12_Faili/Veidenbaums.txt"))   #971

f_list = os.listdir(".") # current dir
print(f_list)
txt_files = [f for f in f_list if f.endswith(".txt")]
print(txt_files)
f_lengths = [(f, file_line_len(f)) for f in txt_files]
print(f_lengths)

# # 1b
def get_poem_lines(fpath):
    with open(fpath, encoding="utf-8") as f:
        clean_list = []
        # x = [line for line in f if "***" not in line]
        for line in f:
            if "***" not in line and len(line)>1:
                # clean_list.append(line.rstrip("\n"))
                clean_list.append(line)
    return clean_list
# print(get_poem_lines("veidenbaums.txt"))

# # 1c
def save_lines(destpath, lines):
    # could add this inside try block if possibility of failure here
    with open(destpath, mode="w", encoding="utf-8") as f:
        f.writelines(lines)

# # 1d
result = get_poem_lines("veidenbaums.txt")
save_lines("veidenbaums_poems.txt",result)

#1e
def clean_punctuation(srcPath, destPath, punct = string.punctuation):
    with open(srcPath, encoding='utf-8') as readFile, open(destPath, mode='w', encoding='utf-8') as writeFile:
        fileContent = readFile.read()
        for symbol in punct:
            fileContent = fileContent.replace(symbol, "")
        writeFile.write(fileContent)


clean_punctuation("veidenbaums_poems.txt", "veid_poems_no_punct.txt")
# clean_punctuation("veidenbaums_poems.txt", "veid_poems_no_punct.txt", punct ="My own characterstring")

for f in txt_files:
    clean_punctuation(f, f+".cleaned.txt")