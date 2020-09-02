# Māras
text = input("ievadi teikumu")
texta = []
words = text.split()
textb = [w[::-1] for w in words]
# for item in words:
#     texta.append(item[::-1])
# textb = " ".join(texta)  # so we do not have " " after last item
print(" ".join(textb))
