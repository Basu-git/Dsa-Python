n=int(input("Enter the number: "))
num=n
reversed=0
while n>0:
    number=n%10
    reversed=reversed*10+number
    n=n//10
print(num==reversed)