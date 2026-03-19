def arm(n):
    num=n
    count=0
    add=0
    while num>0:
        num=num//10
        count+=1
    num=n
    while num>0:
        number=num%10
        add+=number**count
        num=num//10
    print(add==n)
if __name__=="__main__":
    n=int(input("Enter the number: "))
    arm(n)
    