for i in range(1,10):
    line1=''
    line2=''
    for m in range(0,i-1):
        line1 +='          '
    for n in range(i,10):
        line2 +='{} * {}={:>2}  '.format(i,n,i*n)
    print(line1+line2)