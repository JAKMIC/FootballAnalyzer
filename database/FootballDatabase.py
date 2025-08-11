import psycopg2
from psycopg2 import sql, OperationalError


class FootbalDatabase:

    def __init__(self):
        self.host = "localhost"
        self.port = 5432
        self.dbname = "footballanalizer"
        self.user = "postgres"
        self.password = "admin"
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor()
            print("Connected to PostgreSQL")
        except OperationalError as e:
            print(f"Error connecting to PostgreSQL: {e}")
            raise

    def execute(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except Exception as e:
            print(f"Query failed: {e}")
            self.conn.rollback()
            raise

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Connection closed")
