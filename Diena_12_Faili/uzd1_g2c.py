# Vitauts
import tempfile
import random
import string
import urllib.request
from collections import Counter


def saveTmpFileFromUrl(_url):

    tempDir = tempfile._get_default_tempdir()
    tmpName = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    fullName = tempDir + "\\" + tmpName + ".txt"
    urllib.request.urlretrieve(_url, fullName)
    print(f"Temp fails {fullName} izveidots")
    return fullName


def extract_most_common(_strFileName):

    with open(_strFileName, encoding='utf-8') as _file:
        # build a counter from each word in the file
        count = Counter(word for line in _file for word in line.split())
        return count


def main():
    url = 'https://raw.githubusercontent.com/ValRCS/Python_RTU_08_20/master/data/veidenbaums.txt'
    fullFileName = saveTmpFileFromUrl(url)
    # print(extract_most_common(fullFileName)
    all_words = extract_most_common(fullFileName).most_common()
    long_words = [wtuple for wtuple in all_words if len(wtuple[0]) > 4]
    print(long_words[:15])
    # print(extract_most_common(fullFileName).most_common(15))


if __name__ == "__main__":
    main()
