# -*- coding: utf-8 -*-
import os
import sqlite3
import datetime
filePath = "C://Users//VV//AppData//Roaming//Mozilla//Firefox//Profiles//u9am02i1.default-release"

class foxRid:
    def __init__(self):
        self.findPlaces()
        #self.openHTML()
    def findPlaces(self):
        fileList = []
        for file in os.listdir(filePath):
           fileList.append(file)
        if "places.sqlite" in fileList:
            self.main("places.sqlite")
        else:
            print("Couldn't find the places.sqlite file!!")

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn


    def main(self, path):
        database = filePath + "//" + path
        conn = self.create_connection(database)
        with conn:
            self.select_all_tasks(conn)

    def select_all_tasks(self, conn):
        urlList = []
        lastVisit = []
        cur = conn.cursor()
        cur.execute("SELECT * FROM moz_places ORDER BY visit_count DESC")
        rows = cur.fetchall()
        try:
            self.openHTML()
            for row in rows:
                print(str(row[1]))
                if row[8] is not None:
                    with open("report.html", "a") as f1:
                        f1.write("<tr><td class=\"link\">"+str(row[1])+"</td><td>"+str(row[4])+"</td><td>"+
                                 str(datetime.datetime.fromtimestamp(row[8]/1000000))[:str(datetime.datetime.fromtimestamp(row[8]/1000000)).rfind(".")]+"</td></tr>")
            self.closeHTML()
        except:
            pass
        finally:
            f1.close()

    def openHTML(self):
        try:
            with open("file.txt") as f:
                with open("report.html", "w") as f1:
                    for line in f:
                            f1.write(line)
        except:
            pass
        finally:
            f1.close()
            f.close()
    def closeHTML(self):
        try:
            with open("report.html", "a") as f1:
                f1.write("</tbody></table></div></body></html>")
        except:
            pass
        finally:
            f1.close()
foxRid()