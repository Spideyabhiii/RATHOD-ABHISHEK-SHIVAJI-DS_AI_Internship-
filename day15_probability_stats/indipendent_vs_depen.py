import random
trials = 1000
#Independent Events
independent_count = 0
for _ in range(trials):
    coin = random.randint(0, 1)      # 0 = Tails, 1 = Heads
    dice = random.randint(1, 6)      # Dice roll
    if coin == 1 and dice == 6:
        independent_count += 1
independent_probability = independent_count / trials
#Dependent Events
# Two Red marbles without replacement
dependent_count = 0
for _ in range(trials):
    bag = ['R'] * 5 + ['B'] * 5      # 5 Red, 5 Blue
    first = random.choice(bag)
    bag.remove(first)                # Without replacement
    second = random.choice(bag)
    if first == 'R' and second == 'R':
        dependent_count += 1
dependent_probability = dependent_count / trials
#Output Results
print("Independent Event (Heads AND 6)")
print("Experimental Probability:", independent_probability)
print("Theoretical Probability:", 1/12)
print("\nDependent Event (Both Red without replacement)")
print("Experimental Probability:", dependent_probability)
print("Theoretical Probability:", 2/9)
