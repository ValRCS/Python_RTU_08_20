# 1. Simbolu biežums # Marim

def get_char_count(text):
    library_new = dict(
        zip(list(text), [list(text).count(i) for i in list(text)]))
    # print(list(zip(list(text), [list(text).count(i) for i in list(text)])))
    print(library_new)


def main():

    print(get_char_count(
        input("Ievadiet tekstu, kuru jāpārvērš vārdnīcā: ")
    ))


if __name__ == "__main__":
    main()
