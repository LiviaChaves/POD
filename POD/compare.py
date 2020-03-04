def select_max(A, left, right):
    max_pos = left
    i = left
    while i <= right:
        if A[i] > A[max_pos]:
            max_pos = i
        i = i + 1

    return max_pos

def selection_sort(A):
    #print("Ordenando o vetor:")
    for  i in range (len(A) - 1, 0, -1):
        index = select_max(A, 0, i)
        if index != i:
            #print(numbers)
            tmp = A[index]
            A[index] = A[i]
            A[i] = tmp

def insertion_sort(A):
    for k in range(1, len(A)):
        current = A[k]
        j=k

        while j > 0 and A[j - 1] > current:
            A[j] = A[j -1]
            j = j-1

        A[j] = current

def worst_case(size):
    array = []
    for i in range (size -1, -1, -1):
        array.append(i)

    return array

def best_case(size):
    array = []
    for i in range (size):
        array.append(i)

    return array

import random

def median_case(n):
    array = []
    for x in range (n):
        array.append(random.randint(1,n))

    return array


import time

def performance(scenario):
    insertion_times = {}
    selection_times = {}

    size = 10
    while size < 5000:
        array = scenario(size)
        insertion_copy = list(array)
        selection_copy = list(array)

        begin = time.time_ns()
        insertion_sort(insertion_copy)
        end = time.time_ns()
        insertion_times[size] = end - begin

        begin = time.time_ns()
        selection_sort(selection_copy)
        end = time.time_ns()
        selection_times[size] = end - begin

        size = size * 2

    return insertion_times, selection_times

if __name__=="__main__":

    insertion, selection = performance(median_case)

    print("INSERTION:")
    for k, v in insertion.items():
        print('{0}, {1}'.format(k,v))

    print('')

    print("SELECTION:")
    for k, v in selection.items():
        print('{0}, {1}'.format(k,v))


    


   

            