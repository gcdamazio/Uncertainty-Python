import random





# 1. For each of the following, write a function, and repeatedly use it to simulate
#    the probability of an event occurring with the following chances:
#    1. $\frac{2}{7}$

def simulate_2_7(repetitions=10000):
    event_count = 0
    for _ in range(repetitions):
        if random.random() < 2 / 7: 
            event_count += 1
    return event_count / repetitions

#    2. $\frac{1}{10}$
def simulate_1_10(repetitions=10000):
    event_count = 0
    for _ in range(repetitions):
        if random.random() < 1 / 10: 
            event_count += 1
    return event_count / repetitions

#    3. $\frac{1}{100}$
def simulate_1_100(repetitions=10000):
    event_count = 0
    for _ in range(repetitions):
        if random.random() < 1 / 100: 
            event_count += 1
    return event_count / repetitions

#    4. $1$
def simulate_1(repetitions=10000):
  
    return 1


