# arr = [1, 2, 3]
# print(arr[::-1])      # [3, 2, 1]
# arr.reverse()
# print(arr) 

def reverse_array(arr):
    left=0
    right=len(arr)-1

    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr


print(reverse_array([1,2,4,6,7]))