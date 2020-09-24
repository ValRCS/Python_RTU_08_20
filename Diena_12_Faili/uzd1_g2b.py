import os


def file_len(fpath):
    return len(open(fpath, encoding='utf-8').readlines())


def get_poem_lines(fpath):
    lines = []
    with open(fpath, encoding='utf-8') as f:
        for line in f:
            if line.strip():  # something left over means True
                lines.append(line)
    return lines


def main():
    print(file_len("veidenbaums.txt"))
    print(get_poem_lines("veidenbaums.txt"))


if __name__ == "__main__":
    main()
