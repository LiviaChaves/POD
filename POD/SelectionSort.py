def select_max(A, left, right):
    max_pos = left
    i = left
    while i <= right:
        if A[i] > A[max_pos]:
            max_pos = i
        i = i + 1

    return max_pos

def selection_sort(A):
    print("Ordenando o vetor:")
    for  i in range (len(A) - 1, 0, -1):
        index = select_max(A, 0, i)
        if index != i:
            print(numbers)
            #tmp = A[index]
            #A[index] = A[i]
            #A[i] = tmp
            A[index], A[i] = A[i], A[index]  
    

if __name__=="__main__":
    numbers = [25,1,4,3,3,12,2]
    n = str(select_max(numbers, 0, len(numbers)-1))
    print("A posição que contém o maior número é " + n)
    selection_sort(numbers)
    print("Vetor ordenado:")
    print(numbers)