# Vitauts
# r = []

# s = input("Ievadīt teikumu: ")
# # s = "Pirmais otrais Trešais cetrurtais"    # test
# ss = s[0].lower() + s[1:]

# for w in ss.split():
#     r.append(w[::-1])

# ret = " ".join(r)
# if s[0].isupper():
#     ret = ret[0].upper() + ret[1:]

# print(ret)

teksts = input("Ievadi kaut kādu tekstu: ")
# one liner
print(" ".join([word[::-1] for word in teksts.split()]))
# parts = teksts.split()
# new_words = []
# for word in parts:
#     reverse = word[::-1]
#     new_words.append(reverse)
#     # print(reverse, end=" ")
# new_sentence = " ".join(new_words)
# print(new_sentence)
