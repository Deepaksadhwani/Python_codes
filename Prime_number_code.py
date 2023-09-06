n = 10

l1 = [True] * n


for i in range(2,int(n**0.5)):
    if l1[i]:
        for j in range(i*i,n,i):
            l1[j] = False



for i in range(2,len(l1)):
    if l1[i]:
        print(i, end= " ")
