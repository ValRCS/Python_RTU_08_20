# Vitauts
def clean_dict_value(_d, _badVal):
    # retD = {}
    # for k, v in _d.items():
    #     if v != _badVal:
    #         retD[k] = v
    # return retD

    return {k: v for k, v in _d.items() if v != _badVal}


def clean_dict_values_from_List(_d, _vList):
    # retD = {}
    # for k, v in _d.items():
    #     if v not in _vList:
    #         retD[k] = v
    # return retD

    return {k: v for k, v in _d.items() if v not in _vList}


def main():
    print(clean_dict_value({'a': 5, 'b': 6, 'c': 5}, 5))          # -> {'b':6}
    print(clean_dict_values_from_List(
        {'a': 5, 'b': 6, 'c': 5}, [3, 4, 5]))    # -> {'b':6}


if __name__ == "__main__":
    main()
