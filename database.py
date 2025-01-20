from sqlalchemy import create_engine, text
import os

db_conn_str = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_conn_str)

def load_jobs_from_db():
    with engine.connect() as connection:
        print("Connected to the database")
        result = connection.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs
