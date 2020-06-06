mediancomparison = 0

#A method to calculate the median of three numbers using two comparisons
def median(a, b, c):
    if ( a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:
        return c

#A method to partition around the median
def partition_median(array, leftend, rightend):
    left = array[leftend]
    right = array[rightend-1]
    length = rightend - leftend
    if length % 2 == 0:
        middle = array[leftend + length/2 - 1]
    else:
        middle = array[leftend + length/2]
  
    pivot = median(left, right, middle)

    pivotindex = array.index(pivot) #only works if all values in array unique

    array[pivotindex] = array[leftend]
    array[leftend] = pivot

    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1
    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    return i - 1 

 
def quicksort_median(array, leftindex, rightindex):
     global mediancomparison
     if leftindex < rightindex:
         newpivotindex = partition_median(array, leftindex, rightindex)
         mediancomparison += (rightindex - leftindex - 1)
         quicksort_median(array, leftindex, newpivotindex)         
         quicksort_median(array, newpivotindex + 1, rightindex)


if '__name__' == '__main__':
      f = open("input.txt", "r")
      intarray = []
      for line in f:
          intarray.append(int(line))
      f.close()

      #test on an array of length 10000
      mediancomparison = 0
      quicksort_median(intarray, 0, len(intarray))
      print(mediancomparison)
