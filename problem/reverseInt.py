# def reverse_integer(n):
#     negative = n < 0
#     n = abs(n)
#     rev = 0

#     while n != 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n //= 10  # Floor division to remove last digit

#     return -rev if negative else rev

# # Example usage:
# print(reverse_integer(123))    # Output: 321
# print(reverse_integer(-456))   # Output: -654


def reverse_integer(num):
    rev =0
    is_neg = num<0
    num = abs(num)
    while num!=0:
        digit= num%10
        rev= rev*10+digit
        num//=10
    return -rev if is_neg else rev
print(reverse_integer(2345))


    