from f import v11

n=int(input())
a = []
i=0
for i in range(n):
    g=int(input())
    a.append(g)

if v11(n,a):
    print("є")
else:
    print("немає")
