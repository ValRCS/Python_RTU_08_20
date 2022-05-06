from collections import Counter
import string

# def file_line_len(fpath):
#     with open(fpath, encoding = "utf-8") as fin:
#         lines_count = len(fin.readlines()) # only problem we read the file in memory
#     return lines_count

# Task 1a - will work with larger files
def file_line_len(path):
    line_cnt = 0
    with open(path, encoding="utf-8") as f:
        for _ in f: # _ is a placeholder for the line
            line_cnt += 1
    # here file is closed
    return line_cnt
 
# print(file_line_len(path))
src = "veidenbaums.txt"
print(file_line_len("veidenbaums.txt"))

#1b
def get_poem_lines(fpath):
    with open(fpath, encoding='utf-8') as input:
        poem_lines = []
        for line in input:
            if len(line.strip()) !=0 and not line.rstrip().endswith('***'):
                # poem_lines.append(line.rstrip('\n'))
                poem_lines.append(line)
    return poem_lines

#1c,d
def save_lines(fpath, lines, end="\n"):
    with open(fpath, 'w', encoding='utf-8') as fout:
        for line in lines:
            # input.write(line+end)
            fout.write(line)
 
save_lines("Veidenbaums_poems.txt", get_poem_lines(src))

### Task 1e
 

 
def clean_punkts(srcpath,destpath, bad_chars=string.punctuation):
    with open(srcpath, mode = "r", encoding = "utf-8") as fin, open(destpath, mode = "w", encoding = "utf-8") as fout:
        in_text = fin.read()
        # out_text = "".join([char for char in in_text if char not in bad_chars])
        # alternative to above
        
        for bad_char in bad_chars:
            in_text = in_text.replace(bad_char, "")
        fout.write(in_text)
 
clean_punkts("veidenbaums_poems.txt", "veidenbaums_no_vowels.txt")
clean_punkts("veidenbaums_poems.txt", "veidenbaums_no_vowels_m6.txt", bad_chars="aueio")

def get_word_usage(srcpath, destpath, top_n=10):
    """
    funkcija atver failu srcpath un atrod biežāk lietotos vārdus
    :param srcpath: Fails, kuru analizēsim
    :param destpath: fails, ura sagabāsim rezultātus
    :return: True, ja viss izdodās
             False, ja ir kāda kļūda
    """
    if srcpath and destpath:
        with open(srcpath, "r", encoding="utf-8") as my_file:
            split_text = my_file.read().lower().split()
        #     split_txt = " ".join(x[:-2] for x in my_file.readlines()).split(" ")

        my_dict = Counter(split_text)
        most_common = my_dict.most_common(top_n)
        # Veiksim biežāk lietoto vārdu sakārtošanu (no biežākas)
        # sorted_dict = {}
        # sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)
        # for i in sorted_keys:
        #     sorted_dict[i] = my_dict[i]
        # Saglabāsim failā
        with open(destpath, "w", encoding="utf-8") as my_file:
            my_file.write("token, count\n")
            for key, value in most_common:
                my_file.write(f"{key}, {value}\n")
        return True
    return False

get_word_usage("veidenbaums_no_punkts_m6.txt", "veidenbaums_word_usage.csv", top_n=50)