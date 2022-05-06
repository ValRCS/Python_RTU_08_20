from pathlib import Path # this is newer for path manipulation
from string import punctuation
import re
from collections import Counter

# 1a uzdevums
 
# def file_line_len(path,encoding='utf-8'):
#     with open(path, mode="r", encoding=encoding) as f:
#         lines= f.readlines()
#         len_lines=len(lines)
#         print(len_lines)
#     return len_lines

def file_line_len(fpath):
    with open(fpath, encoding="utf-8") as f:  # create a file object
        count = 0
        for _ in f:
            count +=1
    return count

print(file_line_len('veidenbaums.txt'))

def get_poem_lines(fpath:str) -> list:
    """
    Poem lines only skipping empty lines
    We also skip lines ending with ***
    """
    with open(fpath,encoding='utf-8') as f:
        # for line in f:
        #     print(line.rstrip('\n')[-2:])
        fin_list = [line for line in f if len(line.strip())>0 and line.rstrip('\n')[-3:]!='***']
        return fin_list
 
poem_lines = get_poem_lines('veidenbaums.txt')
print(poem_lines[:15])


 
def save_lines(destpath, lines):
    """
    Funkcijas apraksts
    """
    setmode = 'w'
    # if file exists, open in append mode later on
    if Path(destpath).is_file():
        setmode = 'a'
 
    with open(Path(destpath), mode=setmode, encoding='utf-8') as f:
        f.writelines(lines)
 
 
save_lines('veidenbaums_only_poem.txt', poem_lines)


 
def clean_punkts(srcpath, destpath, punctuation=punctuation):
    """
    Funkcijas apraksts
    """
    setmode = 'w'
    # if Path(destpath).is_file():
    #     setmode = 'a'

    punctuation += "“”…"
    
    with open(Path(srcpath), encoding='utf-8') as fin, open(Path(destpath), mode=setmode, encoding='utf-8') as fout:
        for line in fin:
            for p in punctuation:
                line = line.replace(p, "")
            fout.write(line)
            # could do the same with regular expressions
            # fout.write(re.sub('['+punctuation+']','',line))
 
clean_punkts('veidenbaums_only_poem.txt','veidenbaums_no_punkts.txt')



 
def get_word_usage(srcpath, destpath):
    """
    Funkcijas apraksts
    """
    setmode = 'w'
    # if Path(destpath).is_file():
    #     setmode = 'a'
 
    with open(Path(srcpath), encoding='utf-8') as fin, open(Path(destpath), mode=setmode, encoding='utf-8') as fout:
        fintxt = fin.read()
        #print(Counter(fintxt.split()))
        word_counter = Counter(fintxt.lower().split())
        
        # fout.write(str(word_counter.most_common()))
        for word, count in word_counter.most_common():
            fout.write(f"{word}, {count}\n")

get_word_usage('veidenbaums_no_punkts.txt', 'veidenbaums_top_words.txt')
