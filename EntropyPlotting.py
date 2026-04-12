import math
import matplotlib.pyplot as plt

blue_probs = []
entropies = []

p = 1/6
while p <= 5/6:
    p_red = (1 - p) / 2
    p_yellow = p_red

    H = -(p * math.log2(p) +
          p_red * math.log2(p_red) +
          p_yellow * math.log2(p_yellow))

    blue_probs.append(p)
    entropies.append(H)

    p += 0.01

plt.plot(blue_probs, entropies)
plt.xlabel("Probability of Blue")
plt.ylabel("Entropy")
plt.title("Entropy vs Probability of Blue")
plt.grid(True)
plt.show()

