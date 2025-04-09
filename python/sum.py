l=[1,3,4,7,5,2,6,8]
sum=0
for i in range(len(l)):
    if(i%2!=0 and l[i]%2==0):
        sum+=l[i]
        print(sum)
