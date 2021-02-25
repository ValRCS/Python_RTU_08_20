from typing import Collection


from collections import Counter
def get_word_usage(srcpath, destpath):
    with open(srcpath, encoding="utf-8") as f:
        # word_count = Counter(word for line in f for word in line.split())
        word_count = Counter(f.read().split())
    print(word_count.most_common(30))
    return word_count

word_count = get_word_usage("veidenbaums_no_punkts.txt", "anything")
print(word_count['alus'])
print(word_count['mīla'])
print(word_count['krogs'])
print(word_count['svinēt'])
print(word_count['gars'])