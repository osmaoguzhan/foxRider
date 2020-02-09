import sqlite3
from htmlCreator import createHtml as cr

def moz_places(conn):
    cur = conn.cursor()
    cur.execute("SELECT url,visit_count,last_visit_date FROM moz_places ORDER BY visit_count DESC")
    rows = cur.fetchall()
    cr.createTdForURL(rows)

def moz_inputhistory(conn):
    cur = conn.cursor()
    cur.execute("SELECT input,use_count FROM moz_inputhistory ORDER BY use_count DESC")
    rows = cur.fetchall()
    cr.createTdForInput(rows)