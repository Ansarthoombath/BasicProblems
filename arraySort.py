# arr=[23,4,5,56,45]
# arr.sort(reverse=True)
# print(arr)


# def sort_array(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# print(sort_array([9,2,4,5,6,3]))

def sortArray(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
print(sortArray([8,6,7,4,5,2]))
