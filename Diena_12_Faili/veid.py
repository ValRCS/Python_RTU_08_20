with open("../data/veidenbaums.txt", encoding="utf-8") as fstream:
    lines = fstream.readlines()
    # other option is text = fstream.read()
print(lines[:10])