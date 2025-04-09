l=[2,4,6,7,9,15,33]
flag=0
for i in range(len(l)-1):
    if(l[i]>=l[i+1]):
        flah=1
        break
if flag==1:
    print(False)
else:
    print(True)
