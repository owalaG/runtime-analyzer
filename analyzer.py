import time
import random
from demos import quicksort, mergesort

def create_random_list(size, max_val):
    ran_list=[]
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list

size = int(input("What size of list do u want to create? "))
max = int(input("What is the max value of the range? "))

l = create_random_list(size,max)
tic = time.time()
quicksort(l)
toc = time.time()
print("Quicksort elasped time --> ", toc-tic)
tic = time.time()
mergesort(l)
toc = time.time()
print("Mergesort elasped time --> ", toc-tic)
