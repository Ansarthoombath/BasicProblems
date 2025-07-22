def stringcomp(s):
    count=1
    result=""
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            count+=1
        else:
            result+=s[i-1]+str(count)
            count=1
    result+=s[-1]+str(count)
    return result
print(stringcomp("qqqnnmab"))