import os
from sqlalchemy import create_engine, text
# Load credentials from Replit Secrets
DB_USER = os.environ["TIDB_USER"]
DB_PASSWORD = os.environ["TIDB_PASSWORD"]
DB_HOST = os.environ["TIDB_HOST"]
DB_NAME = os.environ.get("TIDB_DB", "tutorial")

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
    print(result_all)