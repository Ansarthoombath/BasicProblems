# def missing_number(arr):
#     actaual_sum=0
#     n= len(arr)+1
#     total_sum = n*(n+1)//2

#     for num in arr:
#         actaual_sum+=num
    
#     return total_sum - actaual_sum

# print(missing_number([1,3,4,5,6]))

# def missing_number(arr):
#     mn = min(arr)
#     mx = max(arr)

#     for num in range(mn, mx +1 ):
#         if num not in arr:
#             return num
#     return None

# print(missing_number([-2,0,1,2,3]))

def miss(arr):
    n= len(arr)
    d=(arr[-1]- arr[0]) //n

    for i in range(n-1):
        expected = arr[i]+d
        if arr[i+1]!=expected:
            return expected
    return None
print(miss([4,8,16,20]))
