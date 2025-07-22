def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
# # print(is_prime(7))

# def print_prime_in_range(start,end):
#     for num in range(start,end+1):
#         if is_prime(num):
#             print(num,end=" ")

# print_prime_in_range(1,20)

def first_n_primes(n):
    primes=[]
    num=2
    while len(primes)<n:
        if is_prime(num):
            primes.append(num)
        num+=1
    return primes
print(first_n_primes(10))


