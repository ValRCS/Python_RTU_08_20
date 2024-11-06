from pathlib import Path
import string # providees some useful constants like string.punctuation
from collections import Counter
print(f"String punctuation: {string.punctuation}")


def count_lines_in_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:

            # lines = file.readlines() # reads ALL into memory!
            # will fail if we don't have enough memory
            # line_len = len(lines)
            # instead we can read line by line
            line_len = 0
            for _ in file: # _ is each line, we don't need it!
                line_len += 1 # does not keep all lines in memory!
            return line_len
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
    
# let's test it on veidenbaums.txt
file_path = 'veidenbaums.txt'
file_len = count_lines_in_file(file_path)
print(f"Number of lines in {file_path}: {file_len}")

# 1b -> uzrakstam funkciju get_poem_lines(fpath), kas atgriež list ar tikai tām rindiņām kurās ir dzeja.
def get_poem_lines(fpath, encoding="utf-8") -> list:
    with open(fpath, encoding=encoding) as file:
        # lines = file.readlines()
        # non_empty_lines = []
        # #for line in lines:
        #    # if line.strip(): # if line is not empty after stripping whitespace
        #         #non_empty_lines.append(line)
        # [non_empty_lines.append(line) for line in lines if line.strip()]
        # lines_without_title = []
        # [lines_without_title.append(line) for line in non_empty_lines if "***" not in line]
        # let's rewrite it work on any size file
        non_empty_lines = []
        for line in file:
            # if not line.strip():
            #     continue # meaning we had a empty line so no need to do anything else and get next line
            # # here we know we have an non empty line guaranteed!
            # if "***" not in line: # we could have used stronger check here like endswith after stripping
            #     non_empty_lines.append(line)
            # alternative is to check both conditions in one if
            if line.strip() and "***" not in line: # if after strip is False no need to check second condition
                non_empty_lines.append(line)
        return non_empty_lines
    
# let's test it on veidenbaums.txt
poem_lines = get_poem_lines(file_path)
# how many
print(f"Number of poem lines in {file_path}: {len(poem_lines)}")

# 1c -> uzrakstam funkciju save_lines(destpath, lines)
def save_lines(destpath, lines, encoding="utf-8"):
    """
    Saves lines to a file at destpath.
    :param destpath: str, destination file path
    :param lines: list, lines to save, lines should have new line characters at the end!
    :param encoding: str, encoding to use
    :return: None
    """
    with open(destpath, mode='w', encoding=encoding) as file:
        # for line in lines:
        #     file.write(line)
        # faster would be
        file.writelines(lines)

# let's test it
# we already have poem_lines from previous task
# destpath = 'veidenbaums_poem.txt'
# save_lines(destpath, poem_lines)

# now we can combine all three functions in one call
# let's read veidenbaums.txt, get only poem lines and save them to veidenbaums_poem.txt
src = 'veidenbaums.txt'
dst = 'veidenbaums_poems.txt'
save_lines(dst, get_poem_lines(src))

# let's create a small function that takes a file name and adds date to it before extension
def get_file_name_with_date(file_name: str|Path, date=None):
    """
    Adds date to file name before extension.
    :param file_name: str, file name
    :param date: str, date to add, if None then current date is used
    :return: str, new file name
    """
    if date is None:
        from datetime import datetime
        date = datetime.now().strftime("%Y_%m_%d")
    # this is hand rolled way to split file name and extension
    # parts = file_name.split('.') # assumes we have only one dot in file name
    # let's use Path from pathlib to do it for us
    # from pathlib import Path # if we do not have it imported yet
    path = Path(file_name)
    stem = path.stem # file name without extension
    ext = path.suffix # extension with dot!
    return f"{stem}_{date}{ext}" 

# let's test it
file_name = 'veidenbaums_poems.txt'
new_file_name = get_file_name_with_date(file_name)
print(new_file_name)

# now let's save it with new name
save_lines(new_file_name, get_poem_lines(src))

# 1e -> uzrakstam funkciju clean_punkts(srcpath,destpath)
def clean_punkts(srcpath, destpath, bad_chars = string.punctuation, encoding='utf-8'):
    with open(srcpath, encoding=encoding) as read_file:
        with open(destpath, mode='w', encoding=encoding) as write_file:
            for line in read_file:
                for c in bad_chars:
                    line = line.replace(c,"")
                write_file.write(line)
 
chars_to_remove = string.punctuation + "„”…" # we can add more characters to remove

clean_punkts('veidenbaums_poems.txt','veidenbaums_clean.txt', bad_chars=chars_to_remove)

# 1f -> uzrakstam funkciju get_word_usage(srcpath, destpath)
# funkcija atver failu un atrod biežāk lietotos vārdus
def get_word_usage(srcpath, destpath, encoding='utf-8'):
    words_list = []
    # with open(srcpath, encoding=encoding) as read_file:
    #     with open(destpath, mode='w', encoding=encoding) as write_file:
    #         for line in read_file:
    #             words_list.extend(line.lower().split())
 
    #         word_counter = Counter(words_list)
    #         write_file.write(str(word_counter))
    # since we are going to be reading all into memory anyway we can do it in one go
    with open(srcpath, encoding=encoding) as read_file:
        words_list = read_file.read().lower().split() # newline is also whitespace so we are good
    word_counter = Counter(words_list)
    # let's write it to file
    with open(destpath, mode='w', encoding=encoding) as write_file:
        # header first
        write_file.write("Word,Count\n")
        for word, count in word_counter.most_common():
            write_file.write(f"{word},{count}\n")
        # in effect we've written a CSV
        # CSV has not strict format but usually it is comma separated values
 
get_word_usage('veidenbaums_clean.txt','veidenbaums_word_count.csv')