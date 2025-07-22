# def second(arr):
#     unique=list(set(arr))
#     unique.sort(reverse=True)
#     return unique[1]
# print(second([23,45,56,24]))

# def lowest(arr):
#     unique=list(set(arr))
#     unique.sort()
#     return unique[1]
# print(lowest([30,23,34,56,21,25,22]))

# arr=[2,3,4,56,77]
# even=sum(i for i in arr if i%2==0)
# odd=sum(i for i in arr if i%2==1)
# print(f"(even:{even} odd:{odd})")

# def missing(arr):
#     n=len(arr)+1
#     actualSum=sum(arr)
#     expextedSum=n*(n+1)//2
#     return expextedSum-actualSum
# print(missing([2,3,5,6,7]))

# def missing(arr):
#     maxi=max(arr)
#     mini=min(arr)
#     expected=sum(range(mini,maxi+1))
#     actual=sum(arr)
#     return expected-actual
# print(missing([-2,0,1,2,3,4]))

# def missing(arr):
#     maxi=max(arr)
#     mini=min(arr)
#     actual_set=set(arr)
#     full_set=set(range(mini,maxi+1))
#     missingnumber=sorted(list(full_set-actual_set))
#     return missingnumber
# print(missing([2,3,4,6,7,9]))

# def missing(arr):
#     maxi=max(arr)
#     mini=min(arr)
#     actualset=set(arr)
#     full_set=set(range(mini,maxi+1))
#     num=sorted(list(full_set-actualset))
#     return num
# print(missing([-2,0,1,3,5]))

# def fib(n):
#    a,b=0,1
#    for i in range(n):
#       print(a,end=" ")
#       a,b=b,a+b
# fib(4)

def prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
print(prime(17))

