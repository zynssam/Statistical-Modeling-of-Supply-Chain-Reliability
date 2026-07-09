import sqlite3
import pandas as pd

print("Loading CSV into SQL Database...")

# 1. Connect to a local database (this creates the file 'logistics.db')
conn = sqlite3.connect('logistics.db')

# 2. Load the CSV into pandas, then push it into our SQL database
df = pd.read_csv('logistics_raw_data.csv')
df.to_sql('shipments', conn, if_exists='replace', index=False)

# 3. Write the SQL Query (The Analytics part)
# We use JULIANDAY() because that is how SQLite calculates differences between dates
query = """
SELECT 
    Carrier,
    COUNT(Order_ID) as Total_Shipments,
    ROUND(AVG(JULIANDAY(Delivery_Date) - JULIANDAY(Ship_Date)), 2) as Avg_Transit_Time,
    SUM(CASE WHEN (JULIANDAY(Delivery_Date) - JULIANDAY(Ship_Date)) <= SLA_Target_Days THEN 1 ELSE 0 END) as On_Time_Deliveries
FROM shipments
GROUP BY Carrier;
"""

# 4. Execute the SQL query and bring the results back
results = pd.read_sql_query(query, conn)

# 5. Calculate the final On-Time Delivery (OTD) Percentage
results['OTD_Percentage'] = round((results['On_Time_Deliveries'] / results['Total_Shipments']) * 100, 2)

print("\n--- EXECUTIVE SUMMARY ---")
print(results[['Carrier', 'Total_Shipments', 'Avg_Transit_Time', 'OTD_Percentage']].to_string(index=False))

# Close the connection
conn.close()