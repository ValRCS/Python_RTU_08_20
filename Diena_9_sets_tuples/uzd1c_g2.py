# Māris
import statistics


def get_min_med_max(_sequence):
    _tuple_res = tuple(min(_sequence))

    if (len(_sequence)/2).is_integer() == False:
        _tuple_res = _tuple_res + (statistics.median(_sequence),)
    else:
        _tuple_res = _tuple_res + \
            (sorted(_sequence)[int(len(_sequence)/2)-1] +
             sorted(_sequence)[int(len(_sequence)/2)],)
    _tuple_res = _tuple_res + (max(_sequence),)

    print(_tuple_res)


def main():

    print(get_min_med_max(
        # ([50, 101, 10.1, 20, 3.1, 40.8])
        # ([2,2,9,9,4,3,2,2])
        # ([1,5,8,4,3,1])
        ("faaacb")
    ))
    print(get_min_med_max(
        ([50, 101, 10.1, 20, 3.1, 40.8])
    ))


if __name__ == "__main__":
    main()
