#1a

def file_line_len(fpath, encoding="utf-8"):
    row_count = 0
    with open(fpath, encoding=encoding) as fstream:
        # row_count = len(fstream.readlines())
        # problem is that fstream.readlines() returns a list
        #  so everything is read into memory
        # usually not a problem, but if file is huge, then it is
        for _ in fstream: # _ is a throwaway variable since we don't need it
            row_count += 1
    return row_count # safer since file is closed
    
# print(file_line_len('Diena_12_Faili\\u1_a4.py'))
print(file_line_len('veidenbaums.txt'))

# 1.b
# Atgriež listu ar tikai tām rindiņām, kurās ir dzeja
# Funkcija nolasa visu failu, pārbauda, vai rindiņa ir tukša vai sākas ar atstarpi
def get_poem_lines(fpath, encoding="utf-8", title_suffix = "***"):
    with open(fpath, encoding=encoding) as file:
        lines = file.readlines()
        poem_lines = []
        for line in lines:
            # so if row has anything
            # and if row does not end with title_suffix
            # we could save the clean line
            clean_line = line.strip()
            if clean_line and not clean_line.endswith(title_suffix):
                # poem_lines.append(clean_line)
                poem_lines.append(line)
    # file is closed here
    return poem_lines
fpath = 'veidenbaums.txt'
poem_lines = get_poem_lines(fpath)
print(poem_lines)  # izvadam listu ar dzejas rindiņām

# 1.c
# Funkcija atver norādīto failu (vai izveido jaunu failu, ja tas vēl nepastāv) 
# Un raksta visu tekstu, kas atrodas padotajā lines listā
def save_lines(destpath, lines, encoding="utf-8", joiner="", mode="w"):
    '''
    destpath - path to file
    lines - list of strings
    encoding - file encoding
    joiner - string that will be used to join lines
    mode - file opening mode (w - write, a - append)
    '''
    with open(destpath, mode=mode, encoding=encoding) as file:
        file.write(joiner.join(lines))

# Saglabā tās veidenbaums_poems.txt failā un izmanto save_lines() funkciju
#1d
fpath = 'veidenbaums.txt'
poem_lines = get_poem_lines(fpath)
destpath = 'veidenbaums_poems.txt'
save_lines(destpath, poem_lines)