
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv", parse_dates=['order_date'])
# Revenue by region
df['revenue'] = df['price'] * df['quantity']
rev = df.groupby('region')['revenue'].sum()
print(rev)

plt.figure()
rev.plot(kind='bar')
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_region.png")
print("Saved revenue_by_region.png")
