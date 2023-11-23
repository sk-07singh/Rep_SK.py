# Selection Sort
arr=[4,8,7,1,2,5,3,6,9,0]
def sel_sort(arr,size):
    for i in range(0,size-1):
        min_term = i
        for j in range(i+1,size):
            if(arr[min_term]>arr[j]):
                min_term=j
        arr[i],arr[min_term]=arr[min_term],arr[i]
print("Before Selection Sort:",arr)
sel_sort(arr,len(arr))
print("After Selection Sort:",arr)
