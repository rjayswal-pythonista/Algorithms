# Programming Assignment 1 - Inversions Calculator

In this first programming assignment we are given [this](https://github.com/rjayswal-pythonista/Algorithms/blob/master/MergeSort/input.txt) long list of integers and our goal is to compute the number of inversions in this file. We should print out exactly the number of these inversions.

The idea is to utilize a sorting algorithm for this task, merge sort in particular. We observe that each time the merge sub routine fetches a number from the "right" subarray we have an inversion. With one additional line of code to our merge subroutine, we were able to count these inversions:
