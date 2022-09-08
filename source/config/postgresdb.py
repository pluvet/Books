import psycopg2
from source.config.env import pg_user, pg_password 

conn = psycopg2.connect(
    user=pg_user,
    password=pg_password,
    host="pgdb",
    port="5432",
    database="books"
)