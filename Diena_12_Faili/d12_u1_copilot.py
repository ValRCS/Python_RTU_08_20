def get_file_line_len(file_name):
    with open(file_name, 'r') as f:
        return len(f.readlines())  # only problem readlines reads all lines into memory

def get_poem_lines(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()  # needs additional filtering