def is_prime(num):
    if num<=1:
        return  False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True



def sum_upto(n):
    total=0
    for i in range(2,n+1):
        if is_prime(i):
            total+=i
    return total
print(sum_upto(10))

# print(is_prime(11))

# def count_prime(start,end):
#     count=0
#     for num in range(start,end+1):
#         if is_prime(num):
#             count+=1
#     return  count      
 

# print(count_prime(1,10))