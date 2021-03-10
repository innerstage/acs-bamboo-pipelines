import pandas as pd
from tabulate import tabulate
from bamboo_lib.helpers import grab_connector, query_to_df


db_connector = grab_connector(__file__, "clickhouse-remote")

query = "select * from acs_ygmt_mortgage_status_by_real_estate_taxes_1 limit 5;"

df = query_to_df(db_connector, query)

print(tabulate(df, headers="keys", tablefmt="psql"))