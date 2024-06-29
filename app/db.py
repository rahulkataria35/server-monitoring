import psycopg2
from psycopg2 import sql
from config import Config

def get_connection():
    conn = psycopg2.connect(
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        host=Config.DB_HOST,
        port=Config.DB_PORT
    )
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP,
            cpu REAL,
            memory REAL,
            disk REAL
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def insert_metrics(timestamp, cpu, memory, disk):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO metrics (timestamp, cpu, memory, disk)
        VALUES (%s, %s, %s, %s)
    ''', (timestamp, cpu, memory, disk))
    conn.commit()
    cur.close()
    conn.close()

def get_recent_metrics():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM metrics ORDER BY timestamp DESC LIMIT 100')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
