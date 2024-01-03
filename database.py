from sqlalchemy import create_engine, text
from sqlalchemy.engine.result import FilterResult
import os

# Replace 'your_username', 'your_password', 'your_host' and 'your_database' with your PostgreSQL credentials
db_username = 'rishabh_career_user'
db_password = os.environ['psw']
db_host = 'singapore-postgres.render.com'
db_name = 'rishabh_career'

# Create a connection string
connection_string = f'postgresql+psycopg2://{db_username}:{db_password}@{db_host}/{db_name}'

# Create an SQLAlchemy engine
engine = create_engine(connection_string)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

    return jobs
