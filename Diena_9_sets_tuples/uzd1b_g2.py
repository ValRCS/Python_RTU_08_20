# Agris 1b
def get_min_med_max(my_list):
    if type(my_list) == str:
        to_list = list(my_list)
        to_list.sort()
        my_list = "".join(to_list)
        mid = int(len(my_list) / 2)
        if len(my_list) % 2 == 1:
            return(min(my_list), my_list[mid], max(my_list))
        else:
            return(min(my_list), (my_list[mid-1] + my_list[mid]), max(my_list))
    else:
        my_list.sort()
        mid = int(len(my_list) / 2)
        if len(my_list) % 2 == 1:
            return(min(my_list), my_list[mid], max(my_list))
        else:
            return(min(my_list), (my_list[mid-1] + my_list[mid])/2, max(my_list))


def main():
    print(get_min_med_max([1, 5, 8, 4, 3]))
    print(get_min_med_max([2, 2, 9, 9, 4, 3]))
    print(get_min_med_max("baaac"))
    print(get_min_med_max("faaacb"))


if __name__ == "__main__":
    main()
