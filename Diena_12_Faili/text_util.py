import os


def file_line_len(fpath):
    return len(open(fpath, 'r', encoding="utf-8").readlines())


def get_poem_lines(fpath):
    with open(fpath, encoding="utf-8") as f:
        poem_lines = [line for line in f if len(
            line.strip()) != 0 and not line.rstrip().endswith("***")]
    # poem = open(fpath, 'r', encoding='utf-8').readlines()
    # poem_lines = []

    # for line in poem:
    #     txtLine = line.replace('\n', '')
    #     if len(txtLine) > 1 and txtLine[-3:] != '***' and txtLine.find('(') < 0:
    #         poem_lines.append(txtLine)
    return poem_lines


def save_lines(destpath, lines):
    with open(destpath, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\r')
    pass


def clean_punkts(srcpath, destpath):
    import string

    with open(destpath, 'w', encoding='utf-8') as f:
        for line in open(srcpath, 'r', encoding='utf-8').readlines():
            line = line.replace('\n', '')
            if set(string.punctuation) & set(line):
                for i in string.punctuation:
                    if i in line:
                        line = line.replace(i, '')
            if len(line) > 0:
                f.write(line + '\r')
    pass


if __name__ == "__main__":
    # print(file_line_len("veidenbaums.txt"))
    # save_lines(os.getcwd() + '/veidenbaums_poems.txt',
    #            get_poem_lines("veidenbaums.txt"))
    # clean_punkts('veidenbaums_poems.txt', 'veidenbaums_no_punkts.txt')
    lines = get_poem_lines("veidenbaums.txt")
    with open("vtest.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)
