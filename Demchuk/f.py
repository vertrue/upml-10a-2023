def v1(B):

    B=[int(i) for i in input().split()]

    max = B[0] 

    for n in range(len(B)):
        if B[n]>max:max=B[n]
    
    return max