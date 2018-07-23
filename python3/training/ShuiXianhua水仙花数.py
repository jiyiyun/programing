import math
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            if 100*x + 10*y +z == pow(x,3) + pow(y,3) + pow(z,3):
                print("ShuiXianHua=",(100*x +10*y+z))
