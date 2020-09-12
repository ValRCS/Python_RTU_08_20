# Arnis
def get_char_count(text):
    result_dict = {}
    for c in text:
        result_dict[c] = text.count(c)
    return result_dict


def get_digit_dict(num):
    digit_dict = get_char_count(str(num))
    return digit_dict


def main():
    my_text = input("ievadiet tekstu: ")
    print(get_char_count(my_text))
    my_digit = input("ievadiet skaitli: ")
    print(get_char_count(my_digit))


if __name__ == "__main__":
    main()
