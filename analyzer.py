import random
import demos

def create_random_list(size, max_val):
    ran_list=[]
    for num in range(size):
        ran_list.append(random.randint(1,max_val))
    return ran_list

size = int(input("What size of list do u want to create? "))
max = int(input("What is the max value of the range? "))
print(type(size), type(max))

print(create_random_list(size, max))
