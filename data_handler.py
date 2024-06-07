import sqlite3

class DataHandler:
    def __init__(self, db_file="health_data.db"):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        # Create the table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id INTEGER PRIMARY KEY,
                weight REAL,
                blood_sugar REAL,
                food_log TEXT,
                date TEXT
            )
        """)
        self.conn.commit()

    def add_data(self, user_id, weight, blood_sugar, food_log, date):
        """
        Adds user data to the database.
        """
        self.cursor.execute("""
            INSERT INTO user_data (user_id, weight, blood_sugar, food_log, date)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, weight, blood_sugar, food_log, date))
        self.conn.commit()

    def get_data(self, user_id):
        """
        Retrieves user data from the database.
        """
        self.cursor.execute("""
            SELECT weight, blood_sugar, food_log, date
            FROM user_data
            WHERE user_id = ?
        """, (user_id,))
        return self.cursor.fetchone()

    def close_connection(self):
        """
        Closes the database connection.
        """
        self.conn.close()