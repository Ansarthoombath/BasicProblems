def change(str,n):
    result="" 
    for ch in str:
        num=ord(ch)-ord('a')
        num=(num+n)%26
        result+=chr(num+ord('a'))
    return result
print(change("abhyz",4))
