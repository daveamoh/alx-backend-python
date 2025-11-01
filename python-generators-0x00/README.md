# Python Generators - Task 0

## Objective
This script connects to a MySQL server, creates the `ALX_prodev` database, defines a `user_data` table, and populates it with data from a CSV file.

## Files
- `seed.py` — main script with database setup and data seeding functions.
- `user_data.csv` — input dataset.
- `0-main.py` — test script provided by ALX.

## Functions
- `connect_db()`: connects to the MySQL server.
- `create_database(connection)`: creates `ALX_prodev` if not exists.
- `connect_to_prodev()`: connects to the `ALX_prodev` database.
- `create_table(connection)`: creates the `user_data` table.
- `insert_data(connection, data)`: inserts rows from CSV into the table.

## Usage
```bash
$ ./0-main.py
