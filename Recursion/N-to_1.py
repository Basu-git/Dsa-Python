def fun(num,n):
    if n>num:
        return
    fun(num,n+1)
    print(n)






if __name__=="__main__":
    n=1
    num=int(input("Enter the number: "))
    fun(num,n)