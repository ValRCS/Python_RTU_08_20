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