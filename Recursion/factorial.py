def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)


if __name__=="__main__":
    num=int(input("Enter the num: "))
    print(f"The factorial of given number is---{fact(num)}")