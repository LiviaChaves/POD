def insertion(A):
    for k in range (1, len(A)):
        current = A[k]
        j = k

        while j > 0 and A[j -1] > current:
            A[j] = A[j-1]
            j = j - 1
        A[j] = current
        print(k,A)   

if  __name__  == '__main__':
    array = [3,2,6,5,7,25,15,26,18]
    insertion(array)

 