# Maijas programma
n = int(input("Ievadi skaitu, cik skaitļus Tu taisies ievadīt: "))
numList = list(int(num) for num in input(
    "Ievadi veselu skaitļu virkni, atdalot skaitļus ar atstarpi: ").strip().split())[:n]


def get_min_avg_max(sequence):
    sorted_list = sorted(numList)
    min = sorted_list[0]
    vid = sum(numList) / n
    max = sorted_list[-1]
    result = min, vid, max
    t = tuple(result)
    return t


res = get_min_avg_max(numList)
print(res)
