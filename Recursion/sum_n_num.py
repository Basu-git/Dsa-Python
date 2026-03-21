def sum(num):
    if num<1:
        return 0
    else:
        return num + sum(num-1)
    





if __name__=="__main__":
    num=int(input("Enter the  N: "))
    print(sum(num))