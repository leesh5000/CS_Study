def reverse_pythonic(s):
    s = s[::-1]
    return s

def reverse(s):
    for i in range(0, len(s)//2):
        temp = s[i]
        s[i] = s[len(s)-1-i]
        s[len(s)-1-i] = temp
    return s

print(reverse_pythonic('hello'))