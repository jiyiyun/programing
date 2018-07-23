L=int(input("L=:"))
for i in range(L):
    if i == 0 or i == (L-1):
        print("*  "*L)
    else:
        print("{} {} {}".format("*"," "*(3*L-6),"*"))