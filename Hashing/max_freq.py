
def freq(arr):
    fre={}
    for i in arr:
        fre[i]=fre.get(i,0)+1
    result=max(fre,key=fre.get)
    return result


"""
result={}
visited=set()
for i in range(len(arr)):
    if arr[i] in visited:
        continue
    count=0
    for j in range(len(arr)):
        if(arr[i]==arr[j]):
            count+=1
            result[arr[i]]=count
            visited.add(arr[i])
return max(result,key=result.get)
"""
    
    
"""Another Approach
def freq(arr):
    result = {}
    visited = set()
    value = 0
    max_key = None

    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        
        result[arr[i]] = count
        visited.add(arr[i])

    for a in result:
        if result[a] > value:
            value = result[a]
            max_key = a

    return max_key
"""
                    



if __name__=="__main__":
    arr=[1,2,1,3,2,2,3,4]
    print(freq(arr))