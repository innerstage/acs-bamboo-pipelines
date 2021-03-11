import pandas as pd
from tabulate import tabulate
from bamboo_lib.helpers import grab_connector, query_to_df


db_connector = grab_connector(__file__, "clickhouse-remote")

query = "show tables"

df = query_to_df(db_connector, query)

print(tabulate(df, headers="keys", tablefmt="psql"))