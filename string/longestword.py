# def longest_word_length(s):
#     words = s.split()
#     max_length = 0
#     for word in words:
#         if len(word) > max_length:
#             max_length = len(word)
#     return max_length

# print(longest_word_length("hello i am ansar"))

def largest(s):
    words=s.split()
    max_length=0
    bigword=""
    for word in words:
        if len(word)>max_length:
            max_length=len(word)
            bigword=word
    return max_length,bigword

# length,word=largest("Hello i am ansar")
# print(length)
# print(word)

# def all_largest_words(s):
#     words = s.split()
#     max_length = 0
#     result = []

#     # First, find the maximum word length
#     for word in words:
#         if len(word) > max_length:
#             max_length = len(word)

#     # Then, collect all words with that max length
#     for word in words:
#         if len(word) == max_length:
#             result.append(word)

#     return max_length, result

# length, words = all_largest_words("Hello i am ansar")
# print("Length:", length)
# print("Words:", words)