n=int(input())
a=[];
for i in range(n):
    a.append(int(input()))
summa=0
for l in range(n):
    if(a[l]%2==0):
        summa+=a[l]
print(summa)