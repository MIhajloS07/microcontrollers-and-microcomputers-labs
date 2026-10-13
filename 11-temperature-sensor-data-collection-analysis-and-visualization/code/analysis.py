import pandas as pd
# Create a DataFrame from the database
df = pd.read_sql("SELECT * FROM dht_data", conn)
# Print the average temperature for each sensor and the average difference between the two sensors
print("Average Temperature (Sensor 1):", df['t1'].mean())
print("Average Temperature (Sensor 2):", df['t2'].mean())
print("Average Temperature Difference:", (df['t1'] - df['t2']).mean())
