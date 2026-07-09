import pandas as pd
import numpy as np
from datetime import timedelta, datetime

# 1. Setup parameters
num_records = 5000
np.random.seed(42)

# Carrier Profiles: (Mean delivery days, Standard Deviation in days)
carriers = {
    'FastFreight': (3.0, 0.5),   # Fast and reliable
    'GlobalShip': (4.0, 1.2),    # Average speed, normal variance
    'BudgetMove': (4.5, 2.8)     # Cheap, highly unreliable (high variance)
}

# 2. Generate Base Data
data = {
    'Order_ID': [f'ORD-{10000 + i}' for i in range(num_records)],
    'Order_Date': [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 180)) for _ in range(num_records)],
    'Carrier': np.random.choice(list(carriers.keys()), num_records, p=[0.4, 0.4, 0.2]),
    'SLA_Target_Days': 4  # The business goal is 4 days
}
df = pd.DataFrame(data)

# 3. Calculate Ship and Delivery Dates based on Carrier Profiles
def calculate_dates(row):
    # Warehouse processing time (1 to 2 days)
    processing_days = np.random.randint(1, 3)
    ship_date = row['Order_Date'] + timedelta(days=processing_days)
    
    # Transit time based on normal distribution of the specific carrier
    mean, std = carriers[row['Carrier']]
    transit_days = max(1, round(np.random.normal(mean, std))) # Can't be less than 1 day
    
    delivery_date = ship_date + timedelta(days=transit_days)
    return pd.Series([ship_date, delivery_date])

df[['Ship_Date', 'Delivery_Date']] = df.apply(calculate_dates, axis=1)

# 4. Save to CSV
df.to_csv('logistics_raw_data.csv', index=False)
print("Success! Created: logistics_raw_data.csv")