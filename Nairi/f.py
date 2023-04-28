def v11 (n,a):
    flag=0
    for i in range(n):
        if a[i]==0:
            flag+=1
    if flag>=3:
        return True
    else:
        return False
