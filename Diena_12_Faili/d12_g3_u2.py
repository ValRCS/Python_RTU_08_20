def get_poem_lines(fpath):
    dzeja = ""
    with open(fpath,mode="r", encoding="utf-8") as f:
        viss_kopaa = f.readlines()
#    dzeja = [line.rstrip("\n") for line in viss_kopaa if line.find("***")==-1 and set(line.lower()) & (set("aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"))]
    # dzeja = [line for line in viss_kopaa if line.find("***")==-1 and set(line.lower()) & (set("aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"))]
    dzeja = [line for line in viss_kopaa if line != "\n" and not line[-4:] == "***\n"]
    return dzeja

def save_lines(destpath, lines):
    with open(destpath, mode="w", encoding="utf-8") as f:
        f.writelines(lines)

save_lines("veidenbaums_poems.txt",get_poem_lines("veidenbaums.txt"))