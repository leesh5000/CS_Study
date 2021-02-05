def Msort(start, end):
    if start < end:
        mid = (start+end)//2
        Msort(start, mid)
        Msort(mid+1, end)

        left = start
        right = mid+1
        temp = []

        while left <= mid and right <= end:
            if arr[left] < arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        if left > mid:
            for i in range(right, end+1):
                temp.append(arr[i])
        else:
            for i in range(left, mid+1):
                temp.append(arr[i])

        idx = 0
        for i in range(start, end+1):
            arr[i] = temp[idx]
            idx += 1


if __name__ == "__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21, 21, 11]
    print(arr)
    Msort(0, len(arr)-1)
    print(arr)
