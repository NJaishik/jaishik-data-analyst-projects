
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bank_transactions.csv", parse_dates=['txn_datetime'])
print("Rows:", len(df))
# Basic aggregations
status_counts = df['status'].value_counts()
print(status_counts)

# Failed transactions by error code
failed = df[df['status']!='SUCCESS']
err = failed['error_code'].value_counts()
print(err)

# Plot: transactions per day
df['date'] = df['txn_datetime'].dt.date
daily = df.groupby('date').size()
plt.figure()
daily.plot()
plt.title("Transactions per day")
plt.xlabel("Date")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("transactions_per_day.png")
print("Saved transactions_per_day.png")
