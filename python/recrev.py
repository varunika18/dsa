def fun(n):
        if n==0:
            return
        if n%2!=0:
            print(n,end=" ")
        fun(n-1)
        if n%2!=0 and n>2:
            print(n,end=" ")
            
       
a=10
fun(a)
        
