import sqlite3
from htmlCreator import createHtml as cr

def formOperations(conn):
    cur = conn.cursor()
    cur.execute("SELECT fieldname,value,timesUsed,firstUsed,lastUsed FROM moz_formhistory ORDER BY timesUsed DESC")
    rows = cur.fetchall()
    cr.createTdForForm(rows)