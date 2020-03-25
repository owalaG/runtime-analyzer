import random
import demos

def create_random_list(size, max_val):
    ran_list=[]
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list

print(create_random_list(40,80))
