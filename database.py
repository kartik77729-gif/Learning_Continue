import os #just imported not in use as in replit there is secrets option while in another we have to create an env file where db_name was saved and impoeted it
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
    result_all = result.all()
    jobs_as_dicts = [row._asdict() for row in result_all]
    print(jobs_as_dicts)