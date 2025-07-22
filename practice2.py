# arr=[2,3,4,1,4,5,6,3]
# arr1=list(set(arr))
# arr1.sort(reverse=True)
# print(arr1[1])


# arr=[2,3,1,3,2,4,5,4,6,7,8,6]
# unique=list(set(arr))
# print(unique)

# def reverse_array(arr):
#     left=0
#     right=len(arr)-1
#     while left<right:
#         arr[left],arr[right]=arr[right],arr[left]
#         left+=1
#         right-=1
#     return arr
# print(reverse_array([5,6,3,8]))


# def freqCount(arr):
#     freq={}
#     for i in arr:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return freq
# print(freqCount([1,2,3,3,4,2,5,6]))

# def freqCount(arr):
#     freq={}
#     for i in arr:
#         if  i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return freq
# print(freqCount([1,2,2,2,4,5,3,3,6,6,9]))

# arr=[1,2,3,8,6,3,8]
# odd=sum(1 for i in arr if i%2!=0)
# even=sum(1 for i in arr if i%2==0)
# print("odd",odd ,"even",even)


