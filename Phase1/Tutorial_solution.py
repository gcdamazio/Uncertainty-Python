import random
from fractions import Fraction

# Step 1: Define the bag
bag = ["Red"] * 5 + ["Blue"] * 7

# Step 2: Define a function to pick a token from the bag
def pick_a_token(container):
    """
    A function to randomly sample from a `container`.
    """
    return random.choice(container)

# Step 3: Define a function for the full experiment
def sample_experiment(bag):
    """
    Samples a token from a given bag and selects a coin with a given probability.
    If the sampled token is red, the probability of selecting heads is 2/3.
    Otherwise, it is 1/2.
    """
    selected_token = pick_a_token(container=bag)

    if selected_token == "Red":
        probability_of_heads = 2 / 3
    else:
        probability_of_heads = 1 / 2

    coin = "Heads" if random.random() < probability_of_heads else "Tails"
    return selected_token, coin

# Step 4: Simulate the experiment many times
number_of_repetitions = 10000
samples = [sample_experiment(bag=bag) for _ in range(number_of_repetitions)]

# Step 5: Calculate probabilities
# Probability of selecting "Heads"
prob_heads = sum(coin == "Heads" for _, coin in samples) / number_of_repetitions

# Probability of selecting "Red" given "Heads"
samples_with_heads = [(token, coin) for token, coin in samples if coin == "Heads"]
prob_red_given_heads = sum(token == "Red" for token, _ in samples_with_heads) / len(samples_with_heads)

# Step 6: Theoretical calculations using fractions
theoretical_prob_heads = (
    Fraction(5, 12) * Fraction(2, 3) + Fraction(7, 12) * Fraction(1, 2)
)
theoretical_prob_red_given_heads = (
    (Fraction(2, 3) * Fraction(5, 12)) / Fraction(41, 72)
)

# Display the results
print("Simulated Probability of Heads:", prob_heads)
print("Theoretical Probability of Heads:", float(theoretical_prob_heads))

print("Simulated Probability of Red given Heads:", prob_red_given_heads)
print("Theoretical Probability of Red given Heads:", float(theoretical_prob_red_given_heads))
