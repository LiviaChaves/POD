class Crianca(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def insertion(A, comparator):
    for k in range(1, len(A)):
        current = A[k]
        j=k

        while j > 0 and comparator(A[j - 1], current) < 0:
            A[j] = A[j -1]
            j = j-1

        A[j] = current
        

def comparador_idades(a,b):
    return b.idade - a.idade

if __name__ == '__main__':
    criancas = [Crianca('jose',5), Crianca('marcos', 4), Crianca('maria', 2)]

    for c in criancas:
        print(c.nome)
    
    insertion(criancas, comparador_idades)

    print()

    for c in criancas:
        print(c.nome)

