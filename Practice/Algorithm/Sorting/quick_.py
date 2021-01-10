# Quick Sorting
# O(nlog(n))

# def quick_sort_pythonic(lt):
#     if len(lt) <= 1:
#         return lt
    
#     pivot = lt[0]
#     left = [i for i in lt[1:] if pivot > i]
#     right = [i for i in lt[1:] if pivot <= i]

#     return quick_sort_pythonic(left) + [pivot] + quick_sort_pythonic(right)

def quick_sort(lt, start, end):
    if start >= end:
        return
    pivot = lt[start]
    left = start
    right = end
    while left < right:
        while lt[left] <= pivot and left < end:
            left += 1
        while lt[right] > pivot and right > start:
            right -= 1
        if left < right:
            lt[left], lt[right] = lt[right], lt[left]
    lt[start], lt[right] = lt[right], lt[start]
    quick_sort(lt, start, right-1)
    quick_sort(lt, right+1, end)

def test(n):
    import random as r
    cnt = 0
    while cnt < n:
        sample_lt = r.sample(range(1000), 100)
        lt = [r.choice(sample_lt) for i in range(100)]
        print('original :', lt)
        quick_sort(lt, 0, len(lt)-1)
        for i in range(len(lt)-1):
            if lt[i] > lt[i+1]:
                return print('sorting failed :', lt)
        print('sorted :', lt)
        cnt+=1
    return print('sorting success')

test(1000)