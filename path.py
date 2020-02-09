# -*- coding: utf-8 -*-
import os
import sqlite3
from htmlCreator import createHtml as cr
from connection import createCon
from operations import mozOp

filePath = "C:\\Users\\VV\\Downloads"

class foxRid:

    def __init__(self):
        self.findPlaces()

    def findPlaces(self):
        fileList = []
        for file in os.listdir(filePath):
           fileList.append(file)
        if "places.sqlite" in fileList:
            self.startOp("places.sqlite")
        else:
            print("Couldn't find the places.sqlite file!!")

    def startOp(self, path):
        database = filePath + "//" + path
        try:
            conn = createCon.create_connection(database)
            with conn:
                cr.openHTML()
                try:
                    mozOp.moz_places(conn)
                    mozOp.moz_inputhistory(conn)
                except:
                    print("While doing operations, got an error!!")
                cr.closeHTML()
        except:
            print("Couldn't connect to the DB!!")
        finally:
            conn.close()



foxRid()