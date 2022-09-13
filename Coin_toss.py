import random	 
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 


random_choose = random.randint(0,1)
if random_choose == 1:
    print("Heads")
else:
    print("Tails")
