import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL, text

# Load environment variables
load_dotenv()

# PostgreSQL connection details
connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 5432)),
    database=os.getenv("DB_NAME")
)

# Create database engine
engine = create_engine(connection_url)

# Test connection
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version()"))
        print("PostgreSQL Connected Successfully!")
        print(result.scalar())

except Exception as e:
    print("Connection Failed:", e)

finally:
    engine.dispose()
 

import pandas as pd

# Read cleaned CSV file
df = pd.read_csv("cleaned_customer_shopping_behavior.csv")

# Upload DataFrame to PostgreSQL
df.to_sql(
    name="customer_behavior",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully!")
print("Total rows uploaded:", len(df))
