# %%
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Save DataFrame to CSV
csv_filename = 'sample.csv'
df.to_csv(csv_filename, index=False)

# Read the CSV file
df_read = pd.read_csv(csv_filename)
print(df_read)
# %%
