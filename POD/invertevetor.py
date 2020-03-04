def invert_array(A):
    print("Vetor recebido:")
    print(A)
    for i in range (len(A) // 2):
        A[i], A[len(A) -1 - i] = A[len(A) -1 - i], A[i]  
    

if __name__=="__main__":
    numbers = [12, 2, 4, 18, 6, 5]
    #n = str(select_max(numbers, 0, len(numbers)-1))
    #print("A posição que contém o maior número é " + n)
    #selection_sort(numbers)
    invert_array(numbers)
    print("Vetor invertido:")
    print(numbers)