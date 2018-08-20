triangle=[[1],[1,1]]
for i in range(2,6):
    cur=[1]
    pre=triangle[i-1]
    for j in range(len(pre)-1):
        cur.append(pre[j] + pre[j+1])
    cur.append(1)
    triangle.append(cur)
print(triangle)