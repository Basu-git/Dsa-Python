def freq(arr):
    
    #Time complexity O(N)
   # Time complexity O(N)

# result = []  # result = [Element, Frequency]
# visited = set()

# for i in arr:
#     if arr[i] in visited:
#         continue
    
#     count = 0
    
#     for j in arr:
#         if arr[i] == arr[j]:
#             count += 1
    
#     result.append([arr[i], count])
#     visited.add(arr[i])

# return result
    #Time complexity O(1)
    fre={}
    for i in arr:
        fre[i]=fre.get(i,0)+1
    result=max(fre,key=fre.get)
    return result
        
                
    
    
    
    
    
    
    
    
    
    
    
    
if __name__=="__main__":
    arr=[1,2,3,2,1,3,4,5]
    print(freq(arr))