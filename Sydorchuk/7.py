import functions as func

    # розмір масиву
n = int(input())
a = []
    
    # введення масиву
for i in range(n):
    a.append(int(input()))
summa = int(0)

    # виведення сума елементів на парних місцях (нумерація з 0)
print(func.summa(n, a))

