def mergesort(arr, n):
    temp = [0]*n
    return _mergesort(arr, temp, 0, n-1)


def _mergesort(arr, temp, left, right):
    if left < right:
        mid = (left+right)//2
        _mergesort(arr, temp, left, mid)
        _mergesort(arr, temp, mid+1, right)
        merge(arr, temp, left, mid, right)
    return arr

def merge(arr, temp, left, mid, right):
    i = left
    j = mid+1
    k = left
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for value in range(left, right+1):
        arr[value] = temp[value]
    return arr

if __name__ == '__main__':
    arr = [4, 1, 5, 3, 2]
    """
    with open('input.txt', 'r') as f:                 # For User Input
        a = f.read().strip('\n').split('\n')
    arr = list(map(int, a))
    """
    n = len(arr)
    result = mergesort(arr,n)
    print(f"Sorted Array found using Fast MergeSort Algorithm: {result}")
