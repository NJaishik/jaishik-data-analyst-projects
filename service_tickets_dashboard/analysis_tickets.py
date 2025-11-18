
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tickets.csv", parse_dates=['created_at'])
# KPI: SLA breach %
sla_pct = df['sla_breach'].mean()*100
print(f"SLA breach %: {sla_pct:.2f}")

# Plot: tickets by severity
sev = df['severity'].value_counts().sort_index()
plt.figure()
sev.plot(kind='bar')
plt.title("Tickets by Severity")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("tickets_by_severity.png")
print("Saved tickets_by_severity.png")
