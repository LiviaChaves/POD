import math


from time import time

def ehPrimo(n):
    result = True
    
    size = int(math.sqrt(n))
    for i in range(2,n):
        #print('{} dividido por {}'.format(n,i))
        if n % i == 0:
            result = False
            break
    return result  

def performance(n):
    rates = {}
    now = time() #marca hora
    ehPrimo(n)
    done = time() # marca hora
    
    diff = (done - now) * 1000
    rates[n] = diff
    print(n,'\t',diff)
     

if __name__ == "__main__":
  for n in range(2,100001):
      performance(n)