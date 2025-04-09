
def fun(i, n):
    if i > n:
        return
    print(i, end=" ")
    fun(i + 1, n)
    if i != n:
        print(i, end=" ")

n = 5
fun(1,n)

