n = 10

l1 = [True] * (n + 1)  

for i in range(2, int(n**0.5) + 1): 
    if l1[i]:
        for j in range(i*i, n + 1, i): 
            l1[j] = False

for i in range(2, len(l1)):
    if l1[i]:
        print(i, end=" ")


