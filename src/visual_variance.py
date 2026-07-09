import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Generating Statistical Distribution Chart...")

# 1. Load the raw data
df = pd.read_csv('logistics_raw_data.csv')

# 2. Convert text dates into actual datetime objects
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'])
df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])

# 3. Calculate exact transit time (in days)
df['Transit_Time'] = (df['Delivery_Date'] - df['Ship_Date']).dt.days

# 4. Set up the visual canvas
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# 5. Create a density plot (Overlapping Bell Curves)
sns.kdeplot(data=df, x='Transit_Time', hue='Carrier', fill=True, common_norm=False, alpha=0.5, linewidth=2)

# 6. Draw the SLA Target Line (The "Deadline")
plt.axvline(4, color='red', linestyle='--', linewidth=2, label='4-Day SLA Target')

# 7. Add professional labels
plt.title('Carrier Reliability: Distribution of Transit Times', fontsize=14, fontweight='bold')
plt.xlabel('Days in Transit', fontsize=12)
plt.ylabel('Density (Frequency of Deliveries)', fontsize=12)
plt.legend()

# 8. Show the chart!
plt.show()