
def prime(num):
    for i in range(2,num):
        if(num%i!=0 and num%num==0):
            print("prime number")
            return
        else:
            print("Not a prime number")
            return
            
            
        
        
if __name__=="__main__":
    num=int(input("Enter the number: "))
    prime(num)
