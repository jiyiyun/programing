lst=["a","b","c","d"]
pwd=["A","B","C","D"]
n = 3
r=0
while n != 0:
    name=input("name:>>>")
    if name in lst:
        password = input("password:>>>")
        if password in pwd:
            print("welcome")
            break
        else:
            print("Passord is wrong")
            r += 1
            n -= 1
            print("rest {} times".format(3 - r))
    else:
        print("Username is wrong")
        n -= 1
        r += 1
        print("rest {} times".format(3-r))