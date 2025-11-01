#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error


def stream_users():
    """
    Generator function that streams rows from the user_data table one by one.
    Yields a dictionary for each user record.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # <-- Update this if you use a MySQL password
            database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data;")

        # Single loop as required
        for row in cursor:
            yield row

    except Error as e:
        print(f"Error streaming users: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
