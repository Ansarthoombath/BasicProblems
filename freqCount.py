arr = [1, 2, 2, 3, 3, 3]
freq = {}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)

 # freq[i] = freq.get(i, 0) + 1