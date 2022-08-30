from database import cursor, db
from rich.console import Console

console = Console()


def getId(website):
    try:
        sql = ("SELECT * FROM passwords WHERE website=%s")
        cursor.execute(sql, (website,))
        result = cursor.fetchone()

        return result[0]
    except:
        return None


def insert(website, username, password):
    sql = ("INSERT INTO passwords(website, username, pass) VALUES (%s, %s, %s)")
    cursor.execute(sql, (website, username, password))
    db.commit()
    console.print(
        f"Added entry for {website} with username: {username}", style="green")


def get():
    sql = ("SELECT * FROM passwords GROUP BY id")
    cursor.execute(sql)
    result = cursor.fetchall()

    return result


def update(website, username, password):
    id = getId(website)
    if id:
        sql = ("UPDATE passwords SET username = %s, pass = %s WHERE id = %s")
        cursor.execute(sql, (username, password, id))
        db.commit()
        console.print(f"Updated entry for {website}", style="green")
    else:
        console.print(
            f"Entry for {website} does not exist.", style="bold italic")


def delete(website):
    id = getId(website)
    if id:
        sql = ("DELETE FROM passwords WHERE id = %s")
        cursor.execute(sql, (id,))
        db.commit()
        console.print(f"Deleted entry for {website}", style="green")
    else:
        console.print(
            f"Entry for {website} does not exist.", style="bold italic")
