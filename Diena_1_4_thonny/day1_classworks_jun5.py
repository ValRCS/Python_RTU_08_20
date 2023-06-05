# print("Dmitry " * 5)
# #Cik būs šogad sekundes?
# print("Šogad būs", 365 * 24 * 60 * 60, "sekundes")
# print(2*3+4*5)
# print(2*(3+4)*5)  # 70 because we changed order
# print("Ba"+"na" * 4 )
# # vārds Banananana, neizmantojot pilnu vārdu, bet zilbes "Ba" un "na"
# print(("Ba"+"na") * 4 )

b="Ba"
n="na"
print(b,n*4) # , is so called seperator
# by default sep is one whitespace
print(f"{b}{n*4}")
print(b,n*4, sep="")  #alternative sep is nothing
print(b+n*4) # b and n are a both strings