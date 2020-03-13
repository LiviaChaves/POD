#DISPENSÃO
#MESMO TAMANHO
# EX: 100,007,999

import math

def create_bucketes(base):
    bucketes = []
    for i in range(base):
        bucketes.append([])
    return bucketes

def sort(items, base):
    tmp = -1
    j = 0
    m = int(math.log(items[0],base)) + 1
    while j < m:
        buckets = create_bucketes(base)
        for number in items:
            tmp = number / math.pow(base,j)
            digit = int(tmp % base)
            buckets[digit].append(number)
        a = 0            

        for buckets in buckets:
          for n in buckets:
            items[a] = n
            a += 1
        j = j + 1

if __name__ == '__main__':
    items = [1012,2053,1443,5152,9008]   
    (sort(items,10))         