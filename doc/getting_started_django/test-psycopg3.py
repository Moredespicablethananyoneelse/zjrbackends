# Note: the module name is psycopg, not psycopg3
import psycopg

# Connect to an existing database
#with psycopg.connect("dbname=test user=postgres") as conn:
with psycopg.connect("host=localhost port= dbname= user= password=") as conn:
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        cur.execute("""drop table if exists test_psycopg3 """)
        # Execute a command: this creates a new table
        cur.execute("""
            CREATE TABLE test_psycopg3 (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """)

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        cur.execute(
            "INSERT INTO test_psycopg3 (num, data) VALUES (%s, %s)",
            (100, "abc'def"))
        cur.execute(
            "INSERT INTO test_psycopg3 (num, data) VALUES (%s, %s)",
            (124, "zjrk"))

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM test_psycopg3")
        cur.fetchone()
        # will return (1, 100, "abc'def")

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()
