def quick_sort(lt: list, start: int, end: int):
    if start < end:
        pivot = lt[start]
        low = start
        high = end

        while low < high:
            while lt[low] <= pivot and low <= end-1:
                low += 1
            while lt[high] >= pivot and high >= start+1:
                high -= 1
            if low <= high:
                lt[low], lt[high] = lt[high], lt[low]
        
        lt[start], lt[high] = lt[high], lt[start]

        quick_sort(lt, start, high-1)
        quick_sort(lt, high+1, end)

lt = [1,1,2,2,3,3,3,3,3, 100,2,3,56,784,2,1,233,4221,22,111,21,234]
quick_sort(lt, 0, len(lt)-1)
print(lt)

