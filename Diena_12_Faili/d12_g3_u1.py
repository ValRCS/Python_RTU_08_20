# def file_line_len(fpath):
#   with open(fpath,encoding="utf-8") as f:
#       line_count = len(f.readlines())
#   print(f"Total lines in file  {line_count}")
#   return line_count

def file_line_len(fpath):
    lnum=0
    with open(fpath,mode="r",encoding="utf-8") as f:
        # res=f.readlines() # we read one big string
        for _ in f: # so this way we do not read all the file in memory this method will on huge files
            lnum += 1
            # if line!="\n":
            #     lnum+=1
    print(lnum)
    return lnum

file_line_len("frost.txt")

# relative path
file_line_len("../data/veidenbaums.txt")

