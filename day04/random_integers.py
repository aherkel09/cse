import random

def get_distribution():
    zeros = [x for x in range(101)]
    distribution = dict.fromkeys(zeros, 0)
    
    for x in range(1000000): # 1 million
        random_int = random.randint(0, 100)
        distribution[random_int] += 1
    
    for d in distribution:
        print(d, distribution[d])

if __name__ == '__main__':
    get_distribution()
    
