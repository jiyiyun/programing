import random

num1=random.randint(1,100)

sum1=0

while True:
    i=int(input("Your Guess Number: \n"))

    if i > num1:
        sum1 += 1
        print("big")
    elif i < num1:
        sum1 += 1
        print("small")
    elif i == num1:
        sum1 += 1
        print("equal,and Your guess %d times" %sum1)
        break
    else:
        print("Wrong")