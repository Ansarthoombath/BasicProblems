# def count_vowles(s):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in s:
#         if char in vowels:
#             count+=1
#     return count
# print(count_vowles("helloo"))

# def str_reversal(s):
#     reverse=""
#     for char in s:
#         reverse=char+reverse
#     return reverse
# print(str_reversal("hello"))

# def longest(s):
#     max_length=""
#     words=s.split(" ")
#     for word in words:
#         if len(word)>len(max_length):
#             max_length=word
#     return max_length
# print(longest("hi iamthe ansar"))

# def nonrepeat(s):
#     repeat=""
#     for i in s:
#         if s.count(i)==1:
#             repeat+=i
#     return repeat if repeat else None
    
# print(nonrepeat("hello"))

# def removeDuplicate(s):
#     result=""
#     for char in s:
#         if char not in result:
#             result+=char
#     return result
# print(removeDuplicate("ansar"))

def freq(s):
    frequency={}
    for char in s:
       if char in frequency:
           frequency[char]+=1
       else:
           frequency[char]=1
    return frequency
print(freq("aabbccd"))
