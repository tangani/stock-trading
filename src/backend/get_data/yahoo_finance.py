import psycopg2


def get_data(database, table):
    conn = psycopg2.connect(
        database=f"{database}", user='postgres', password='password', host='127.0.0.1', port='5432'
    )

    conn.autocommit = True

    cursor = conn.cursor()
    cursor.execute(f"""SELECT * from {table}""")

    data = cursor.fetchall()
    conn.commit()
    conn.close()

    return data


if __name__ == "__main__":
    get_data("postgres", "yahoo_finance")

