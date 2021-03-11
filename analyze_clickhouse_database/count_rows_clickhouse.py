import pandas as pd
from tabulate import tabulate
from bamboo_lib.helpers import grab_connector, query_to_df


db_connector = grab_connector(__file__, "clickhouse-remote")

# Get table names
names_df = query_to_df(db_connector, "SHOW TABLES")
tables = names_df["name"].tolist()

# Print row count
for t in tables:
    print("\n\nTABLE: {}".format(t))

    query = "SELECT COUNT(*) FROM {};".format(t)
    df = query_to_df(db_connector, query)
    print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))