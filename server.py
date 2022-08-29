from database import cursor, db


def insert(website, username, password):
    sql = ("INSERT INTO passwords(website, username, pass) VALUES (%s, %s, %s)")
    cursor.execute(sql, (website, username, password))
    db.commit()
    insert_id = cursor.lastrowid
    print("\033[92m {}\033[00m" .format(
        f"Added entry for {website} with username: {username}"))


def get():
    sql = ("SELECT * FROM passwords GROUP BY id")
    cursor.execute(sql)
    result = cursor.fetchall()

    return result


def update(website, username, password):
    sql = ("UPDATE passwords SET username = %s, pass = %s WHERE website = %s")
    cursor.execute(sql, (username, password, website))
    db.commit()
    print("\033[92m {}\033[00m" .format(f"Updated entry for {website}"))


def delete(website):
    sql = ("DELETE FROM passwords WHERE website = %s")
    cursor.execute(sql, (website,))
    db.commit()
    print("\033[92m {}\033[00m" .format(f"Deleted entry for {website}"))
