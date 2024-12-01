import random



# 3. An experiment consists of selecting a token from a bag and spinning a coin. The bag contains 3 red tokens and 4 blue tokens. A token is selected at random from the bag, its colour is noted and then the token is returned to the bag.
#    When a red token is selected, a biased coin with probability $\frac{4}{5}$ of landing heads is spun.
#    When a blue token is selected, a biased coin with probability $\frac{2}{5}$ of landing heads is spun.

# Function to simulate drawing a token and flipping a coin
def simulate_experiment(bag):
    token = random.choice(bag)  # Choose a token
    if token == "Red":
        # Probability of heads when red is chosen
        coin = "Heads" if random.random() < 4/5 else "Tails"
    else:  # Blue token
        # Probability of heads when blue is chosen
        coin = "Heads" if random.random() < 2/5 else "Tails"
    return token, coin

#    1. Approximate the probability of picking a red token?
def simulate_red_token_probability(bag, repetitions=10000):
    red_count = 0
    for _ in range(repetitions):
        token, _ = simulate_experiment(bag)  # Ignore the coin outcome for this calculation
        if token == "Red":
            red_count += 1
    return red_count / repetitions

#    2. Approximate the probability of obtaining Heads?
def simulate_heads_probability(bag, repetitions=10000):
    heads_count = 0
    for _ in range(repetitions):
        _, coin = simulate_experiment(bag)
        if coin == "Heads":
            heads_count += 1
    return heads_count / repetitions

#    3. If a heads is obtained, approximate the probability of having selected a red token.
def simulate_conditional_red_given_heads(bag, repetitions=10000):
    red_given_heads_count = 0
    heads_count = 0
    for _ in range(repetitions):
        token, coin = simulate_experiment(bag)
        if coin == "Heads":
            heads_count += 1
            if token == "Red":
                red_given_heads_count += 1
    return red_given_heads_count / heads_count if heads_count > 0 else 0

# Define the bag with 3 red tokens and 4 blue tokens
bag = ["Red"] * 3 + ["Blue"] * 4

# 1. Approximate the probability of picking a red token
red_probability = simulate_red_token_probability(bag)
print(f"Approximate probability of picking a red token: {red_probability}")

# 2. Approximate the probability of obtaining heads
heads_probability = simulate_heads_probability(bag)
print(f"Approximate probability of obtaining heads: {heads_probability}")

# 3. Approximate the probability of having selected a red token if heads is obtained
conditional_red_given_heads = simulate_conditional_red_given_heads(bag)
print(f"Approximate probability of having selected a red token given heads: {conditional_red_given_heads}")
