import psycopg2


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "shopnest_db",
    "user": "postgres",
    "password": "Stat@123"
}


def get_connection():
    """
    Returns a PostgreSQL database connection.
    """
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        return connection

    except Exception as error:
        print(f"Database Connection Error: {error}")
        return None