# arr=[1,2,3,2,4,5,6,4]
# unique=list(set(arr))
# second=arr[1]
# print(unique)
# print(second)

arr= [2,3,1,2,3,4,5,6,5,4]
unique = []
for num in arr:
  if num not in unique:
    unique.append(num)
print(unique)