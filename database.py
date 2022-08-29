import mysql.connector

config = {
    'user': "root",
    'password': 'Hy_Database',
    'host': 'localhost',
    'database': 'passwordManager'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
