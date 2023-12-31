# Given an unsorted integer array, find a pair with the given sum in it.
def find_pair(arr, k):
    for i in range(len(arr)-1):
        for j in range(i + 1 , len(arr)):
            if arr[i] + arr[j] == k:
                print("Pair: (",arr[i],",",arr[j],")")
                return
    print("No Pair found")
arr=[1,5,8,7,4,2,3]
k = 7
find_pair(arr , k)
