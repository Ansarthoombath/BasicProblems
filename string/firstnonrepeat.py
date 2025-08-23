
# def first_non_repeating(s):
#     for ch in s:
#         if s.count(ch) == 1:
#             return ch
#     return None  # or return '_'
    
# # Example usage
# text = "aabbcdeff"
# print("First non-repeating character:", first_non_repeating(text))  # Output: c


# def norepeat(s):
#     result=[]
#     for char in s:
#         if s.count(char)==1:
#             result.append(char)
#     return result 
# print(norepeat("aabccdeefgghh"))

def nonrep(s):
    result=[]
    for ch in s:
        if s.count(ch)==1:
            result.append(ch)
    return result

print(nonrep("aabbccdffeggg"))