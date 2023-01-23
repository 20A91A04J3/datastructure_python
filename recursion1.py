def fun(num):
    if num==0:
        return
    fun(num-1)
    print(num,end=' ')
n=5
fun(n)
