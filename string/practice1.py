

# def count_vowels(s):
#     count=0
#     vowels='aeiouAEIOU'
#     for char in s:
#         if char in vowels:
#             count+=1
#     return count
# print(count_vowels("anuman"))

# def reverse(str):
#     reversed="" 
#     for char in str:
#         reversed=char+reversed
#     return reversed
# print(reverse("hello"))

# def duplicate(str):
#     unique="" 
#     for char in str:
#         if char not in unique:
#             unique+=char
#     return unique
# print(duplicate("helloo"))

# def frequency(str):
#     freq={}
#     for char in str:
#         if char in freq:
#             freq[char]+=1
#         else:
#             freq[char]=1
#     return freq
# print(frequency("ansart"))

# def frequency(str):
#     freq={}
#     for char in str:
#         if char in freq:
#             freq[char]+=1
#         else:
#             freq[char]=1
#     return freq
# print(frequency("abbbccdde"))

# def removeDup(str):
#     unique=""  
#     for char in str:
#         if char not in unique:
#             unique+=char
#     return unique
# print(removeDup("ansart"))

# def largest(s):
#     words=s.split()
#     max_length=0
#     bigword=""
#     for word in words:
#         if len(word)>max_length:
#             max_length=len(word)
#             bigword=word
#     return max_length,bigword

# length,word=largest("Hello i am ansar")
# print(length)
# print(word)

# def norepeat(s):
#     for char in s:
#        if s.count(char)==1:
#            return char 
#     return None
# print(norepeat("aabbcde"))

# def norepeat(s):
#     result=[]
#     for char in s:
#         if s.count(char)==1:
#             result.append(char)
#     return result 
# print(norepeat("aabccdeefgghh"))

# def compress(s):
#     count=1
#     compressed=""
#     for i in range(1,len(s)):
#         if s[i]==s[i-1]:
#             count+=1
#         else:
#             compressed+=s[i-1]+str(count)
#             count=1
#     compressed+=s[-1]+str(count)
#     return compressed
# print(compress("aabbccde"))
    

# def compress(s):
#     result=""
#     count=1
#     for i in range(1,len(s)):
#         if s[i]==s[i-1]:
#             count+=1
#         else:
#             result+=s[i-1]+str(count)
#             count=1
#     result+=s[-1]+str(count)
#     return result
# print(compress("aabcccddee"))

# def feb(n):
#     a,b=0,1
#     for _ in range(n):
#         print(a,end=" ")
#         a,b=b,a+b
# feb(5)

def feb(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b
feb(3)
