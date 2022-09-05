import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()

config = {
    'user': os.getenv("USER"),
    'password': os.getenv("PASSWORD"),
    'host': os.getenv("HOST"),
    'database': os.getenv("DATABASE")
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
