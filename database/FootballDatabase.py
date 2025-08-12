import psycopg2
from psycopg2 import sql, OperationalError
from dotenv import load_dotenv
import os


class FootbalDatabase:

    def __init__(self):
        load_dotenv(dotenv_path="./vars.env")
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                dbname=os.getenv("DB_DATABASE"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
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
