from flask import jsonify
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


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * from jobs where id = :val'),
                              {"val": id})
        job = []
        for row in result.all():
            job.append(row._asdict())
            if len(row) == 0:
                return None
            else:
                return dict(job[0])
