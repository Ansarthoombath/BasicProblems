# arr = [10, 20, 5, 40, 40]
# unique = list(set(arr))
# unique.sort(reverse=True)
# print(unique[1])  # Output: 20


arr= [2,1,3,4,5]

largest = arr[0]
second= arr[0]

for num in arr:
    if num>largest:
        second =largest
        largest = num
    elif num>second and num!=largest:
        second = num
print(second)
        