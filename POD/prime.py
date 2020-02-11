import math

def ehPrimo(n):
    result = True
    
    size = int(math.sqrt(n))
    for i in range(2,size):
        #print('{} dividido por {}'.format(n,i))
        if n % i == 0:
            result = False
            break
    return result       

if __name__ == "__main__":
    n=991564654552145
    #n=23

    print(ehPrimo(n))   