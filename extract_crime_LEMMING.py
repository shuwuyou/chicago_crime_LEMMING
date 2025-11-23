import requests
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# ==============================================
# CONFIG
# ==============================================
URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

START_DATE = "2024-10-01T00:00:00"
END_DATE   = "2025-10-01T00:00:00"

BATCH_SIZE = 50000   # API max
offset = 0

all_data = []

print("Downloading Chicago Crime Data from 2024-10-01 to 2025-10-01...")

# ==============================================
# PAGINATION LOOP
# ==============================================
while True:
    params = {
        "$limit": BATCH_SIZE,
        "$offset": offset,
        "$order": "date DESC",
        "$where": f"date >= '{START_DATE}' AND date < '{END_DATE}'"
    }

    resp = requests.get(URL, params=params)
    batch = resp.json()

    if not batch:
        print("No more rows. Finished downloading.")
        break

    df_batch = pd.DataFrame(batch)
    print(f"Fetched {len(df_batch)} rows at offset {offset}")

    all_data.append(df_batch)
    offset += BATCH_SIZE

# ==============================================
# CONCAT ALL BATCHES
# ==============================================
df = pd.concat(all_data, ignore_index=True)
print("Total rows downloaded:", len(df))


# ==============================================
# SELECT COLUMNS + CLEAN
# ==============================================
cols = [
    "id","case_number","date","primary_type","description",
    "location_description","arrest","domestic","district",
    "ward","community_area","latitude","longitude"
]

df = df[cols]
df.columns = [c.upper() for c in df.columns]


# ==============================================
# LOAD INTO SNOWFLAKE
# ==============================================
print("Loading into Snowflake...")

conn = snowflake.connector.connect(
    user="LEMMING",
    account="sfedu02-azb79167",
    private_key_file="/Users/shuwuyou/rsa_key.p8",
    warehouse="TRAINING_WH",
    database="MLDS430",
    schema="final_LEMMING",
    role="TRAINING_ROLE"
)

# Clear table before inserting new data
conn.cursor().execute("DELETE FROM raw_crime_LEMMING")

# Write dataframe into Snowflake
write_pandas(conn, df, "RAW_CRIME_LEMMING")

conn.close()

print("Load complete.")
