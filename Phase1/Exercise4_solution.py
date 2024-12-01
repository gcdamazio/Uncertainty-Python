import random



# 4. On a randomly chose day, the probability of an individual travelling to school by car, bicycle or on foot is $1/2$, $1/6$ and $1/3$ respectively. The probability of being late when using these methods of travel is $1/5$, $2/5$ and $1/10$ respectively.

# Probabilities
P_car = 1/2
P_bicycle = 1/6
P_foot = 1/3

P_late_car = 1/5
P_late_bicycle = 2/5
P_late_foot = 1/10

# 1. Approximate the probability that an individual travels by foot and is late
def simulate_foot_and_late(repetitions=10000):
    foot_and_late_count = 0
    for _ in range(repetitions):
        travel_choice = random.choices(["Car", "Bicycle", "Foot"], [P_car, P_bicycle, P_foot])[0]
        if travel_choice == "Foot":
            late_probability = P_late_foot
            is_late = random.random() < late_probability
            if is_late:
                foot_and_late_count += 1
    return foot_and_late_count / repetitions

# 2. Approximate the probability that an individual is not late
def simulate_not_late(repetitions=10000):
    not_late_count = 0
    for _ in range(repetitions):
        travel_choice = random.choices(["Car", "Bicycle", "Foot"], [P_car, P_bicycle, P_foot])[0]
        if travel_choice == "Car":
            late_probability = P_late_car
        elif travel_choice == "Bicycle":
            late_probability = P_late_bicycle
        else:
            late_probability = P_late_foot
        is_late = random.random() < late_probability
        if not is_late:
            not_late_count += 1
    return not_late_count / repetitions

# 3. Given that an individual is late, approximate the probability that they did not travel on foot
def simulate_not_foot_given_late(repetitions=10000):
    not_foot_given_late_count = 0
    late_count = 0
    for _ in range(repetitions):
        travel_choice = random.choices(["Car", "Bicycle", "Foot"], [P_car, P_bicycle, P_foot])[0]
        if travel_choice == "Car":
            late_probability = P_late_car
        elif travel_choice == "Bicycle":
            late_probability = P_late_bicycle
        else:
            late_probability = P_late_foot
        is_late = random.random() < late_probability
        if is_late:
            late_count += 1
            if travel_choice != "Foot":
                not_foot_given_late_count += 1
    return not_foot_given_late_count / late_count if late_count > 0 else 0

# Run simulations
foot_and_late_prob = simulate_foot_and_late()
print(f"Approximate probability that an individual travels by foot and is late: {foot_and_late_prob}")

not_late_prob = simulate_not_late()
print(f"Approximate probability that an individual is not late: {not_late_prob}")

not_foot_given_late_prob = simulate_not_foot_given_late()
print(f"Approximate probability that an individual did not travel on foot given they are late: {not_foot_given_late_prob}")
