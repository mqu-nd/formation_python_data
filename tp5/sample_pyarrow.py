# %%
import pyarrow as pa
import pyarrow.parquet as pq

# Creation d'une table PyArrow simple
data = {
    'nom': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35],
    'salaire': [70000, 50000, 60000]
}
table = pa.Table.from_pydict(data)
print(table)

# Conversion en DataFrame pandas
df = table.to_pandas()
print(df.head())

# Sauvegarde en Parquet
pq.write_table(table, "data.parquet")

# Lecture depuis un fichier Parquet
table_from_file = pq.read_table("data.parquet")

# %%
