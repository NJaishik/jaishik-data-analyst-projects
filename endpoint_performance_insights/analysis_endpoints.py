
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("endpoints.csv", parse_dates=['last_seen'])
# Patch compliance %
pc = (df['patch_status']=='Compliant').mean()*100
print(f"Patch compliance %: {pc:.2f}")

# Plot: CPU distribution (histogram)
plt.figure()
df['cpu_percent'].hist(bins=20)
plt.title("CPU % Distribution")
plt.xlabel("CPU %")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("cpu_distribution.png")
print("Saved cpu_distribution.png")
