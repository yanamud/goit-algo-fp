import random
from collections import defaultdict

import matplotlib.pyplot as plt

nums = 1_000_000

counts = defaultdict(int)

for _ in range(nums):
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    dice = dice_one + dice_two
    counts[dice] += 1

probabilities = {key: count / nums for key, count in counts.items()}

sorted_probabilities = dict(sorted(probabilities.items()))

teoretical_probabilities = {2: 0.0278, 
                            3: 0.0556, 
                            4: 0.0833, 
                            5: 0.1111, 
                            6: 0.1389, 
                            7: 0.1667, 
                            8: 0.1389, 
                            9: 0.1111, 
                            10: 0.0833, 
                            11: 0.0556, 
                            12: 0.0278}

print("------|-------------|-----------|--------")
print("Dice  | Prob-actual | Prob-teor | Diff-ty")
print("------|-------------|-----------|--------")
for dice, prob in sorted_probabilities.items():
    if dice in teoretical_probabilities:
        print(f"{dice: < 5} | {prob:.2%}       | {teoretical_probabilities[dice]:.2%}     | {prob - teoretical_probabilities[dice]:.2%}")

plt.bar(probabilities.keys(), probabilities.values())  # noqa
plt.show()