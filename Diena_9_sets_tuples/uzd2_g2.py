# Vitauts
def get_common_elements(*args):
    ret = set(args[0])
    for a in args[1:]:
        ret = ret.intersection(set(a))

    return tuple(ret)


def main():
    # Argumentu virknes virknes būt list,tuple,string.
    # -> ('b',)
    print(get_common_elements("abc", ['a', 'b'], ('b', 'c')))
    # -> ('b','d')
    print(get_common_elements("abcd", ['a', 'b', 'd'], ('b', 'c', 'd')))


if __name__ == "__main__":
    main()
