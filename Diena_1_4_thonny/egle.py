augstums=int(input("Ievadiet eglītes augstumu:"))
tuksums=" "
zvaigzne="*"
 
tuksumi=augstums-1
zvaigznes=1
for i in range(augstums):
    print(tuksums*tuksumi + zvaigzne*zvaigznes + tuksums*tuksumi)
    zvaigznes+=2
    tuksumi-=1