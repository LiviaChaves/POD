def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint - 1)
        quickSortHelper(alist,splitpoint + 1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]

    letfmark = first + 1
    rightmark = last

    done = False
    while not done:
        while letfmark <= rightmark and alist[letfmark] <= pivotvalue:
            letfmark = letfmark + 1
        while alist [rightmark] >= pivotvalue and rightmark >=letfmark:
            rightmark = rightmark - 1
        if rightmark < letfmark:
            done = True
        else:
            temp = alist[letfmark]
            alist[letfmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark
if __name__ == "__main__":
    alist = [65,25,12,45,3,5,58,67,33,22]
    print(alist)
    quickSort(alist)
    print(alist)