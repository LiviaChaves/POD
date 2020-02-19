class Crianca(object):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

def insertion(A, comparador):
    for k in range (1, len(A)):
        current = A[k]
        j = k

        while j > 0 and comparador(A[j -1] , current) < 0:
            A[j] = A[j - 1]
            j = j - 1
        A[j] = current
        print(k,A)   

def comparador_idades(a,b):
    return b.idade - a.idade

if  __name__  == '__main__':
    criancas = [Crianca('jose',5),Crianca('Marcos',4) ,Crianca('Maria',2)]

for c in criancas:
    print(c.nome)

insertion(criancas, comparador_idades)
print(c.nome)

for c in criancas:
    print(c.nome)

