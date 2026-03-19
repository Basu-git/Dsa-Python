def pattern1(rows):
    for i in range(1,rows+1):
        print("*"*rows+" ")
def pattern2(rows):
    for i in range(1,rows+1):
        print("*"*i+" ")
def pattern3(rows):
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print(str(j),end=" ")
        print("") 
def pattern4(rows):
    for i in range(1,rows+1):
       print(i,end="")
       
def pattern5(rows):
    for i in range(rows):
            print("*"*(rows-i),end="")   
            print("")  
def pattern6(rows):
    for i in range(1,rows+1):
        for j in range(1,rows-(i-1)+1):
            print(j,end="")
        print()
def pattern7(rows):
    for i in range(1,rows+1):
        print(" "*(rows-i)+"*"*(2*i-1)+" "*(rows-i))
def pattern8(rows):
    for i in range(rows):
        print(" "*(i)+"*"*(2*rows-2*i-1)+" "*(i))
def pattern9(rows):
    for j in range(rows):
        print(" "*(rows-j)+"*"*(2*j+1)+" "*(rows-j))
    for j in range(rows):
        print(" "*(j)+"*"*(2*rows-2*j-1)+" "*j)     
def pattern10(rows):
    for i in range(2*rows-1):
        if i<rows:
            print("*"*(i+1))
        else:
            print("*"*(2*rows-i-1))

def pattern11(rows):
    for i in range(1,rows+1):
        if i%2==0:
            start=0
        else:
            start=1
        for j in range(1,i+1):
            print(start,end=' ')
            start=1-start
        print()
def pattern12(rows):
    for i in range(1, rows+1):
    
        for j in range(1, i+1):
            print(j, end="")

    
        spaces = 2 * (rows - i)
        print(" " * spaces, end="")

        
        for j in range(i, 0, -1):
            print(j, end="")

        print()
def pattern13(rows):
    c=1
    for  i in range(1,rows+1):
        for j in range(1,i+1):
            print(c,end=" ")
            c+=1
        print()
def pattern14(rows):
    for i in range(rows):
        for j  in range(i+1):
            print(chr(65+j),end=" ")
        print()
def pattern15(rows):
    for i in range(rows):
        for j in range(rows-i):
            print(chr(65+j),end=" ")
        print()
def pattern16(rows):
    for i in range(rows):
        for j in range(i+1):
            print(chr(65+i),end=" ")
        print()             
def pattern17(rows):
    for i in range(rows):
        print(" "*(rows-i-1),end="")
        for j in range(i+1):
            print(chr(65+j),end="")
        for j in range(i-1,-1,-1):
            print(chr(65+j),end="")
        print()
def pattern18(rows):
    for i in range(rows):
        for j in range(i+1):
            print(chr(65+rows-j-1),end=" ")
        print()
def  pattern19(rows):
    for i in range(rows):
        print("*"*(rows-i)+" "*(2*i)+"*"*(rows-i))
    for i in range(rows):
        print("*"*(i+1)+" "*2*(rows-i-1)+"*"*(i+1))

rows=int(input("Enter the number of rows: "))
pattern19(rows)