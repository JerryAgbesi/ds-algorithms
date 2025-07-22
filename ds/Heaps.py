def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

def buildHeap(arr, N):
  
    start = N // 2 - 1
  
    for i in range(start, -1, -1):
        heapify(arr, N, i)  

    return arr         

array = [3,9,2,1,4,5,12]
length = len(array)



print(buildHeap(array,length))     