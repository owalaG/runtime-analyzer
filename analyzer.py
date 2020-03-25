import time
import random
from demos import quicksort, mergesort, bubblesort

def create_random_list(size, max_val):
    ran_list=[]
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list


def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc - tic
    print("{}\t -> elasped time: {} seconds" .format(func_name.__name__.capitalize(), seconds))


size = int(input("What size of list do u want to create? "))
max = int(input("What is the max value of the range? "))

l = create_random_list(size,max)
analyze_func(bubblesort,l.copy()) #use copy to avoid sorted array being parsed 
analyze_func(quicksort,l)
analyze_func(mergesort,l)
