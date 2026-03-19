def fun(num,n):
    if n>num:
        return
    print(n)
    fun(num,n+1)
    






if __name__=="__main__":
    n=1
    num=int(input("Enter the number: "))
    fun(num,n)