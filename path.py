# -*- coding: utf-8 -*-
"""
The tool which gets important data from Firefox DB.
Author Oguzhan OSMA
"""

import os
import sqlite3
from htmlCreator import createHtml as cr
from connection import createCon
from operations import mozOp
from operations import formOp

filePath = "C:\\Users\\VV\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\u9am02i1.default-release"

class foxRid:

    def __init__(self):
        cr.openHTML()
        self.fileList = []
        for file in os.listdir(filePath):
            self.fileList.append(file)
        self.findPlaces()
        self.findForm()

    def findPlaces(self):
        if "places.sqlite" in self.fileList:
            self.startOp("places.sqlite")
        else:
            print("Couldn't find the places.sqlite file!!")

    def findForm(self):
        if "formhistory.sqlite" in self.fileList:
            self.formOp("formhistory.sqlite")
        else:
            print("Couldn't find the form history DB file!!")

    def startOp(self, path):
        database = filePath + "//" + path
        try:
            conn = createCon.create_connection(database)
            with conn:
                try:
                    mozOp.moz_places(conn)
                    mozOp.moz_inputhistory(conn)
                    mozOp.moz_bookmarks(conn)
                except:
                    print("While doing operations, got an error!!")
        except:
            print("Couldn't connect to the DB!!")
        finally:
            conn.close()

    def formOp(self, path):
        database = filePath + "//" + path
        try:
            conn = createCon.create_connection(database)
            with conn:
                try:
                    formOp.formOperations(conn)
                except:
                    print("While doing operations, got an error!!")
        except:
            print("Couldn't connect to the DB!!")
        finally:
            conn.close()

    def __del__(self):
        cr.closeHTML()


foxRid()