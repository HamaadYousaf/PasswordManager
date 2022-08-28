from database import cursor, db


def insert(website, username, password):
    sql = ("INSERT INTO passwords(website, username, pass) VALUES (%s, %s, %s)")
    cursor.execute(sql, (website, username, password))
    db.commit()
    insert_id = cursor.lastrowid
    print(f"Added entry for {website} with username: {username}")


def get():
    sql = ("SELECT * FROM passwords GROUP BY id")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)


def update(id, username, password):
    sql = ("UPDATE passwords SET username = %s, pass = %s WHERE id = %s")
    cursor.execute(sql, (username, password, id))
    db.commit()
    print(f"Updated entry for {id}")


def delete(id):
    sql = ("DELETE FROM passwords WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()
    print(f"Deleted entry for {id}")


delete(1)
get()
