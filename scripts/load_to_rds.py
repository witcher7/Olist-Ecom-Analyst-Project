import pandas as pd
import os 
from sqlalchemy import create_engine
from dotenv import load_dotenv  

load_dotenv()

username = os.getenv("RDS_USERNAME")
password = os.getenv("RDS_PASSWORD")
host = os.getenv("RDS_HOST")
database = os.getenv("RDS_DATABASE")
engine = create_engine(f"postgresql://{username}:{password}@{host}/{database}")

df = pd.read_parquet("cleaned_data/final_product_analytics.parquet")
print("Loading data to RDS...")

chunk_size = 100000
for i in range(0, len(df), chunk_size):
    df_chunk = df.iloc[i:i+chunk_size]
    df_chunk.to_sql("product_analytics", engine, if_exists="append", index=False,chunksize=chunk_size,method="multi")
    print(f"Loaded rows {i} to {i+chunk_size} into RDS...")


    # SSMS _-> SQL Server Management Studio
    # pgAdmin --> PostgreSQL
    # MySQL Workbench --> MySQL

    