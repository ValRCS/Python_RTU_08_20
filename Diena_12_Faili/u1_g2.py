def file_line_len(fpath = '../data/veidenbaums.txt'):
    ln_len = 0
    with open(fpath, encoding="utf-8") as veden:
        for _ in veden:
            ln_len += 1
    return ln_len

print(file_line_len())

def get_poem_lines(fpath):
    lines = []
    with open(fpath, encoding='utf-8') as f:
        for line in f:
            if line.strip() and not line.endswith("***\n"):  # something left over means True
                lines.append(line)
    return lines
 
print(get_poem_lines("../data/veidenbaums.txt")[:10])

def save_lines(destpath, lines, encoding="utf-8"):
    with open(destpath, 'x', encoding=encoding) as f:
        f.writelines(lines)
        # below we would use if we wanted to add/change to some lines
        # for line in lines:
        #     f.write(line)      

save_lines("veid_2.txt", get_poem_lines("../data/veidenbaums.txt"))