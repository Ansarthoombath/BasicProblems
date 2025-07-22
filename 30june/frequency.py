def freq_count(s):
    frequency={}
    for char in s:
        frequency[char]=frequency.get(char,0)+1
    return frequency
print(freq_count("swiss"))
