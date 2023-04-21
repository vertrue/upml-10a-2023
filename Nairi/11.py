n=int(input())
zer=0
numb=[]
for i in range(n):
	numb.append(int(input()))
	if numb[i]==0:
		zer+=1
	if zer>=3:
		print("є")
		break
if zer<3:
	print("нема")