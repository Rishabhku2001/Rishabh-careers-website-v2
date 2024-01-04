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


def load_job_from_db(id):
  with engine.connect() as conn:
    query = text("select * from jobs where id = :val")
    result = conn.execute(query, {'val': id})
    row = result.all()
    if len(row) == 0:
      return None
    else:
      return row[0]._asdict()


def add_application_to_DB(job_id, data):
  with engine.connect() as conn:
    print("hellow")
    job_id = job_id
    full_name = data.get('full_name')
    email = data.get('email')
    linkedin_url = data.get('Linkedin_url')
    education = data.get('education')
    work_experience = data.get('work_experience')
    resume_url = data.get('resume_url')
    query = text(
        f"INSERT INTO application (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ('{job_id}', '{full_name}' ,'{email}','{linkedin_url}', '{education}' ,'{work_experience}', '{resume_url}')"
    )
    print(query)
    conn.execute(query)
    conn.commit()
