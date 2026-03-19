def div(num):
    n=1
    while n<=num:
        if(num%n==0):
            print(n,end=" ")
        n+=1
if __name__=="__main__":
    num=int(input("Enter the number: "))
    div(num)