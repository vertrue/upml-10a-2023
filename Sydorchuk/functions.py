def summa(n, a):
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += a[i]
    return sum
