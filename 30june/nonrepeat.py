# def first_non_repeat(s):
#     for char in s:
#         if s.count(char)==1:
#             return char
#     return None
# print(first_non_repeat("swiss"))


def non_repeat(s):
   
        
    return [char for char in s if s.count(char)==1]   
print(non_repeat("swiss"))


