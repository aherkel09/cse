import random

def get_distribution():
    distribution = [0 for x in range(100)]
    
    for x in range(1000000): # 1 million
        random_int = random.randint(0, 100)
        distribution[random_int] += 1
        # more later
    
