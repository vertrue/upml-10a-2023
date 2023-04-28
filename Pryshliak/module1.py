def v10(n, a):
    summ=0
    for i in range(n):
        if i%2==0:
            summ+=a[i]
    return summ
