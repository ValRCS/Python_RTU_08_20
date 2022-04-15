a = 3
b = 3
c = 9
# print(a < b < c)
# print(a < b <= c < 9000)
if a<b and a<c:
    print (a)
    if b<c:
        print (b,"\n",c,sep="")
    else:
        print (c,"\n",b,sep="")
else:
    if b<a and b<c:
        print (b)
        if a<c:
            print (a,"\n",c,sep="")
        else:
            print (c,"\n",a,sep="")
    else:
        print(c)
        if a<b:
            print (a,"\n",b,sep="")
        else:
            print (b,"\n",a,sep="")