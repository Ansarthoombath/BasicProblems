# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()    

# 1
# 12
# 123
# 1234
# 12345

# n=5
# count=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(count,end="")
#         count+=1
#     print()
# 1
# 23
# 456
# 78910
# 1112131415

# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     print()    

#     1
#    12
#   123
#  1234
# 12345

# n=4
# count=1
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(i):
#         print(count,end="")
#         count+=1
#     print()
#    1
#   23
#  456
# 78910

# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,2*i):
#         print(j,end="")
#     print()

#     1
#    123
#   12345
#  1234567
# 123456789




# n=4
# for i in range(1,n+1):
#     for j in range(i):
#         print((i+j)%2,end="")
#     print()

# 1
# 01
# 101
# 0101

# 

# 0
# 10
# 010
# 1010
# 01010

n=5
count=1
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(count,end="")
        count+=1
    print()
