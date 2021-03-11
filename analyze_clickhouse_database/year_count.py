import pandas as pd
from tabulate import tabulate
from bamboo_lib.helpers import grab_connector, query_to_df


db_connector = grab_connector(__file__, "clickhouse-remote")

# Get table names
names_df = query_to_df(db_connector, "SHOW TABLES")
tables = names_df["name"].tolist()

# Print row count
for t in [table for table in tables if "acs" in table]:
    print("\nTABLE: {}".format(t))

    query = "SELECT year, COUNT(*) FROM {} GROUP BY year ORDER BY year;".format(t)
    df = query_to_df(db_connector, query, col_headers=["year", "count"])
    new_df = pd.DataFrame({
        "year": df["year"].tolist(),
        "count": ["{:,}".format(int(c)) for c in df["count"]]
    })
    print(tabulate(new_df, headers="keys", tablefmt="psql", showindex=False))