import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n, m = map(int, input().split())
    a = list(sorted(list(map(int, input().split()))))
    def binary_search(lt, start, end, target):
        mid = (start + end)//2
        if target == lt[mid]:
            return mid
        if target > lt[mid]:
            return binary_search(lt, mid+1, end, target)
        else:
            return binary_search(lt, start, mid, target)
    print(binary_search(a, 0, len(a)-1, m)+1)