def mergesort(arr, n):
    temp = [0]*n
    return _mergesort(arr, temp, 0, n-1)


def _mergesort(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left+right)//2
        inv_count += _mergesort(arr, temp, left, mid)
        inv_count += _mergesort(arr, temp, mid+1, right)
        inv_count += merge(arr, temp, left, mid, right)
    return inv_count

def merge(arr, temp, left, mid, right):
    i = left
    j = mid+1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
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
    return inv_count

if __name__ == '__main__':
    #arr = [4, 1, 5, 3, 2]
    with open('input.txt', 'r') as f:                            #input file contains unsorted array of order of 10^6
        a = f.read().strip('\n').split('\n')
    arr = list(map(int, a))
    n = len(arr)
    start = time.time()
    result = mergesort(arr,n)
    end = time.time()
    print(f"Number of inversions found using Fast MergeSort Algorithm is done in {end-start} secs: {result}")
