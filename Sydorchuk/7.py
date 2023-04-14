    # розмір масиву
n = int(input())
a = []
    
    # введення масиву
for i in range(n):
    a.append(int(input()))
    # сума елементів на парних місцях (нумерація з 0)
summa = int(0)
for i in range(n):
    if i % 2 == 0:
        summa += a[i]
        
    
    # виведення
print(summa)

