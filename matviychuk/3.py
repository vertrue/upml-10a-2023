'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

a=[int(i) for i in input().split()]
n=0
for i in range(0,len(a)):
    if a[i]==0:
        n+=1
print(n)
