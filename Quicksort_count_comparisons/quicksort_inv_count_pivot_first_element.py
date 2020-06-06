def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    inv_count = 0
    for j in range(low+1, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            inv_count += high-1
            i += 1
    arr[low], arr[i-1] = arr[i-1], arr[low]
    return i-1, inv_count

def quicksort(arr, low, high):
    inv_count = 0
    if low < high:
        pindex, inv_count = partition(arr, low, high)
        inv_count += quicksort(arr, low, pindex)
        inv_count += quicksort(arr, pindex+1, high)
    return inv_count


if __name__ == '__main__':
    #arr = [7, 5, 1, 4, 3, 2, 6]
    #print(f"Enter Space Separated Array values for Quicksort: ")
    #arr = list(map(int, input().split()))
    with open('input.txt', 'r') as f:
        arr = f.read().strip('\n').split('\n')  #Input for array of length 10^6
    n = len(arr)
    inversion = quicksort(arr, 0 , n)
    print(f"Inversion: {inversion}")
