# Uzd. Nr.3
 
# sk_a = int(input("Enter number a "))
# sk_b = int(input("Enter number b "))
# sk_c = int(input("Enter number c "))

sk_a, sk_b, sk_c = 15, 12, 12
 
print (f"You have entered numbers {sk_a}, {sk_b}, {sk_c}")
 
print ("Checking number sequence.....")
# if sk_a <= sk_b and sk_b <= sk_c: # same as next line
if sk_a <= sk_b <= sk_c: 
    print(" Result is: {sk_a}, {sk_b}, {sk_c}") 
    print(f" Result is: {sk_a}, {sk_b}, {sk_c}") 
elif sk_a <= sk_c <= sk_b:
    print(" Result is: {sk_a}, {sk_c}, {sk_b}")
    print(f" Result is: {sk_a}, {sk_c}, {sk_b}")
elif sk_b <= sk_a <= sk_c:
    print(" Result is: {sk_b}, {sk_a}, {sk_c}")
    print(f" Result is: {sk_b}, {sk_a}, {sk_c}")
elif sk_b <= sk_c <= sk_a:
    print(" Result is: {sk_b}, {sk_c}, {sk_a}")
    print(f" Result is: {sk_b}, {sk_c}, {sk_a}")
elif sk_c <= sk_a <= sk_b:
    print(" Result is: {sk_c}, {sk_a}, {sk_b}")
    print(f" Result is: {sk_c}, {sk_a}, {sk_b}")
else: #{sk_c}, {sk_b}, {sk_a}
    print(" Result is: {sk_c}, {sk_b}, {sk_a}")
    print(f" Result is: {sk_c}, {sk_b}, {sk_a}")