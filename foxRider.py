# -*- coding: utf-8 -*-
"""
The tool which gets important data from Firefox DB.
Author Oguzhan OSMA
"""

import os
import argparse
import sqlite3
import time
from htmlCreator import createHtml as cr
from connection import createCon
from operations import mozOp
from operations import formOp

class foxRid:

    def __init__(self):
        self.banner()
        self.filePath = input("Please type the path of Firefox Profile:")
        if len(self.filePath) != 0:
            cr.openHTML()
            print("\rCreating Report[               ] - %0", end="")
            time.sleep(1)
            self.fileList = []
            for file in os.listdir(self.filePath):
                self.fileList.append(file)
            print("\rCreating Report[######         ] - %33", end="")
            self.findPlaces()
            print("\rCreating Report[############   ] - %66", end="")
            self.findForm()
            print("\rCreating Report[###############] - %100", end="")
        else:
            print("Path is missed!!")

    def banner(self):
        print(" _____         ____  _     _\n"
              "|  ___|____  _|  _ \(_) __| | ___ _ __ \n"
              "| |_ / _ \ \/ / |_) | |/ _` |/ _ \ '__|\n"
              "|  _| (_) >  <|  _ <| | (_| |  __/ |   \n"
              "|_|  \___/_/\_\_| \_\_|\__,_|\___|_|   \n")

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
        database = self.filePath + "//" + path
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
        database = self.filePath + "//" + path
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
        print("\nReport Location : " + str(os.getcwd()) + "\\report.html")

if __name__ == '__main__':
    foxRid()