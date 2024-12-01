import random

# 2. Write a function, and repeatedly use it to simulate the probability of
#    selecting a red token from each of the following configurations:




def simulate_red_token_probability(bag, repetitions=10000):
    red_count = 0
    for _ in range(repetitions):
        token = random.choice(bag)  
        if token == "Red":
            red_count += 1  
    return red_count / repetitions
   
   #    1. A bag with 4 red tokens and 4 green tokens.
bag1 = ["Red"] * 4 + ["Green"] * 4
probability_1 = simulate_red_token_probability(bag1)
print(f"Probability of selecting a red token (4 Red, 4 Green): {probability_1}")

#    2. A bag with 4 red tokens, 4 green tokens and 10 yellow tokens.
bag2 = ["Red"] * 4 + ["Green"] * 4 + ["Yellow"] * 10
probability_2 = simulate_red_token_probability(bag2)
print(f"Probability of selecting a red token (4 Red, 4 Green, 10 Yellow): {probability_2}")

#    3. A bag with 0 red tokens, 4 green tokens and 10 yellow tokens.
bag3 = ["Green"] * 4 + ["Yellow"] * 10  # No red tokens
probability_3 = simulate_red_token_probability(bag3)
print(f"Probability of selecting a red token (0 Red, 4 Green, 10 Yellow): {probability_3}")
