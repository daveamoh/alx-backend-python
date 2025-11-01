#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error


def stream_users_in_batches(batch_size):
    """
    Generator that fetches rows from the user_data table in batches.
    Yields a list of user dictionaries (one batch at a time).
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Update if your MySQL has a password
            database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data;")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch  # yield one batch at a time

    except Error as e:
        print(f"Error streaming users in batches: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def batch_processing(batch_size):
    """
    Processes each batch to filter users over the age of 25.
    Prints each user dictionary that meets the condition.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)
