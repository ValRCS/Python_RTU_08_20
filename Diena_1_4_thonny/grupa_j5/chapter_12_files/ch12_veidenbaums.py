import string

def file_line_len(fpath):
    try:
        with open(fpath, 'r', encoding='utf-8') as file:
            # this would fail on large files
            # lines = file.readlines()
            # if you suspect large files use this instead
            count = 0
            for _ in file: # we do not care about contents of the line
                count += 1
            return count
    except FileNotFoundError:
        print(f"Fails '{fpath}' netika atrasts!")
        return 0 # Ja neatrod failu, atgriež '0' rindiņas jeb t.s. fallback value
    
print(file_line_len('LICENSE.md'))
print(file_line_len('LICENSE'))
print(file_line_len('data/veidenbaums.txt'))

##########
# 1b Task
##########

def get_poem_lines(fpath, encoding='utf-8'):
    good_lines = []
    try:
        with open(fpath, mode='r', encoding=encoding) as f:
            for line in f:
                # we check if line is not empty and does not contain '***'
                if line.strip() and '***' not in line:
                    # print(line)
                    good_lines.append(line)
    except FileNotFoundError:
        print(f"File '{fpath}' not found!")
        return [] # return empty list if file not found
    # return when file is closed
    return good_lines

poem_lines = get_poem_lines('veidenbaums.txt')
print(f"Found {len(poem_lines)} lines in poem")
# i know I have veidenbaums.txt file data directory
# so I use relative path
poem_lines = get_poem_lines('data/veidenbaums.txt')
print(f"Found {len(poem_lines)} lines in poem")

##########
# 1c Task
##########

def save_lines(destpath, lines, encoding='utf-8'):
    with open(destpath, 'w', encoding=encoding) as f:
        for line in lines:
            f.write(line)

# let's create a timestamped file
import datetime
now = datetime.datetime.now()
print(now)
# let's format the date
print(now.strftime('%Y-%m-%d_%H-%M-%S'))
# let's use ISO format
# print(now.isoformat())
time_suffix = now.strftime('%Y_%m_%d_%H_%M_%S')
# now i each time i run the script i will get a new file
# save_lines(f'data/veidenbaums_clean_{time_suffix}.txt', poem_lines)
save_lines(f'data/veidenbaums_clean.txt', poem_lines)

def clean_punkts(srcpath, destpath, bad_chars=string.punctuation):
    try:
        with open(srcpath, 'r', encoding='utf-8') as src_file:
            text = src_file.read()
            cleaned_text = ''.join(char for char in text if char not in bad_chars)
        
        with open(destpath, 'w', encoding='utf-8') as dest_file:
            dest_file.write(cleaned_text)
        
        print(f"Attīrītais fails saglabāts: '{destpath}'.")
    except FileNotFoundError:
        print(f"Fails '{srcpath}' netika atrasts!")

#
# clean_punkts('data/veidenbaums_clean.txt', 'data/veidenbaums_clean_no_punct.txt')
# turns out we also need to clean …
# simply create a new string with bad chars
bad_chars = string.punctuation + '…'
clean_punkts('data/veidenbaums_clean.txt', 'data/veidenbaums_clean_no_punct.txt', bad_chars)

# let's count most common words and save results to a csv file
def count_words_and_save(src, dst=None, lowercase=True):
    # count words in src
    # save results to dst
    # we will use collections.Counter
    # https://docs.python.org/3/library/collections.html#collections.Counter
    import collections
    # we will use csv module to save results
    # https://docs.python.org/3/library/csv.html
    import csv
    # we will use pathlib to work with paths
    # https://docs.python.org/3/library/pathlib.html
    from pathlib import Path
    
    with open(src, encoding="utf-8") as f:
        text = f.read()
    
    if lowercase:
        text = text.lower()
    # we need to split text into words
    words = text.split()
    # we need to count words
    word_counts = collections.Counter(words)
    # we need to sort words by count
    # https://docs.python.org/3/library/collections.html#collections.Counter.most_common
    # most_common([n]) Return a list of the n most common elements and their counts from the most common to the least.
    top_words = word_counts.most_common() # list of of tuples [('word', count), ...]
    # we need to save results to csv file
    # https://docs.python.org/3/library/csv.html#csv.writer
    # if dst is None we will use src with .csv extension !
    if dst is None:
        dst = Path(src).with_suffix('.csv') # i converte src to Path object and change extension to .csv
    # we need to open csv file for writing
    with open(dst, 'w', encoding="utf-8") as f:
        # we need to create csv writer
        writer = csv.writer(f, lineterminator="\n") # we could specify delimiter, quotechar, quoting, etc. here
        # we need to write header, avoid newline
        writer.writerow(['word', 'count'])
        # we need to write rows
        writer.writerows(top_words)

# let's test
count_words_and_save('data/veidenbaums_clean_no_punct.txt')