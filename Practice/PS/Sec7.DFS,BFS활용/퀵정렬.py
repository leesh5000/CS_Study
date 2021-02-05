'''
병합정렬은 후위순회
퀵정렬은 전위순회
'''


def Qsort(start, end):
    if start < end:
        pivot = arr[start]
        left = start
        right = end

        while left < right:
            while arr[left] <= pivot and left < end:
                left += 1
            while arr[right] > pivot and right > start:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        arr[start], arr[right] = arr[right], arr[start]
        Qsort(start, right-1)
        Qsort(right+1, end)


if __name__ == "__main__":
    # arr = [7, 2, 5, 3, 1, 8, 4, 6, 4, 4]
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20]
    print(arr)
    Qsort(0, len(arr)-1)
    print(arr)
