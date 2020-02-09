# -*- coding: utf-8 -*-
import os
import datetime

def openHTML():
    try:
        with open("htmlCreator/file.txt") as f:
            with open("report.html", "w") as f1:
                for line in f:
                        f1.write(line)
    except:
        pass
    finally:
        f1.close()
        f.close()


def createTdForURL(rows):
    try:
        for row in rows:
            if row[2] is not None:
                with open("report.html", "a") as f1:
                    f1.write("<tr><td class=\"link\">" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" +
                                str(datetime.datetime.fromtimestamp(row[2] / 1000000))[
                                :str(datetime.datetime.fromtimestamp(row[2] / 1000000)).rfind(".")] + "</td></tr>")
            else:
                with open("report.html", "a") as f1:
                    f1.write(
                        "<tr><td class=\"link\">" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>None</td></tr>")
    except:
        pass
    finally:
        f1.close()

def createTdForInput(rows):
    try:
        with open("report.html", "a") as f1:
            f1.write("<table class=\"table\" id=\"input\">"
                     "<thead><tr><th>Keyword</th><th>Keyword Rate</th></tr></thead><tbody>")
        for row in rows:
            print(row)
            with open("report.html", "a") as f:
                    f.write("<tr><td class=\"link\">" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>")
    except:
        pass
    finally:
        f.close()
        f1.close()


def closeHTML():
    try:
        with open("report.html", "a") as f1:
            f1.write("</tbody></table></div></body></html>")
    except:
        pass
    finally:
        f1.close()