import os
from sqlalchemy import create_engine, text

# Load credentials from Replit Secrets
for key in ["TIDB_USER", "TIDB_PASSWORD", "TIDB_HOST", "TIDB_DB"]:
    if not os.environ.get(key):
        raise EnvironmentError(f"Missing secret: '{key}'. Add it in the Secrets tab (padlock icon) in Replit.")

DB_USER = os.environ["TIDB_USER"]
DB_PASSWORD = os.environ["TIDB_PASSWORD"]
DB_HOST = os.environ["TIDB_HOST"]
DB_NAME = os.environ["TIDB_DB"]

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    "?charset=utf8mb4&ssl_verify_cert=true&ssl_verify_identity=true",
    pool_recycle=300,   # avoid stale connections timing out on TiDB Cloud
    pool_pre_ping=True, # verify connection health before using
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    result_all = result.all()  # store once — calling .all() twice will return [] the second time
    print("type(result):", type(result))
    print("type(result_all):", type(result_all))
    first_result_all = result_all[0]
    print("type(first_result_all):", type(first_result_all))
    print(result_all)
    dict_result_all = dict(result_all[0])
    print(dict_result_all)