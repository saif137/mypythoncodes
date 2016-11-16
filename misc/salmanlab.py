def BSort(n):
    for i in range(len(n)-1):
        for j in range(i,len(n)):
            if n[i]<n[j]:
                temp = n[j]
                n[j] = n[i]
                n[i] = temp

def sum(n):
    sum = 0
    max=[]
    while n:
        max.append(n % 10)
        n = n // 10
    BSort(max)
    print(max)
    for i in (max):
        sum = sum + i
    print(sum)


sum(32156)

