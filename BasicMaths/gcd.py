def gcd(num1,num2):
    num=1
    div=min(num1,num2)
    gc=1
    while num<=div:
        if(num1%num==0 and num2%num==0):
            gc=num
        num+=1
    print(gc)     
if __name__=="__main__":
    print("Enter the two number: ")
    num1=int(input())
    num2=int(input())
    gcd(num1,num2)