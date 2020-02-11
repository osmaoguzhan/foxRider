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
        with open("report.html", "a") as f2:
            f2.write("</tbody></table>")
        f2.close()
        f1.close()

def createTdForInput(rows):
    try:
        with open("report.html", "a") as f1:
            f1.write("<table class=\"table table-striped table-bordered\" id=\"input\">"
                     "<thead><tr><th>Keyword</th><th>Keyword Rate</th></tr></thead><tbody>")
        for row in rows:
            print(row)
            with open("report.html", "a") as f:
                    f.write("<tr><td class=\"link\">" + str(row[0]) + "</td><td>" + str(row[1]) + "</td></tr>")
    except:
        pass
    finally:
        with open("report.html", "a") as f2:
            f2.write("</tbody></table>")
        f2.close()
        f.close()
        f1.close()

def createTdForBookmark(rows):
    try:
        with open("report.html", "a") as f1:
            f1.write("<table class=\"table table-striped table-bordered\" id=\"bookmark\">"
                     "<thead><tr><th>Title</th><th>Date Added</th><th>Last Modified</th></tr></thead><tbody>")
        for row in rows:
            print(row)
            with open("report.html", "a") as f:
                    f.write("<tr><td class=\"link\">" + str(row[0]) + "</td><td>" + str(datetime.datetime.fromtimestamp(row[1] / 1000000))[
                                :str(datetime.datetime.fromtimestamp(row[1] / 1000000)).rfind(".")] + "</td><td>"+str(datetime.datetime.fromtimestamp(row[2] / 1000000))[
                                :str(datetime.datetime.fromtimestamp(row[2] / 1000000)).rfind(".")]+"</td></tr>")
    except:
        pass
    finally:
        with open("report.html", "a") as f2:
            f2.write("</tbody></table>")
        f2.close()
        f.close()
        f1.close()

def createTdForForm(rows):
    try:
        with open("report.html", "a") as f1:
            f1.write("<table class=\"table table-striped table-bordered\" id=\"formhistory\">"
                     "<thead><tr><th>Field Name</th><th>Value</th><th>Times Used</th><th>First Used</th><th>Last Used</th></tr></thead><tbody>")
        for row in rows:
            print(row)
            with open("report.html", "a") as f:
                    f.write("<tr><td class=\"link\">" + str(row[0]) + "</td><td class=\"link\">"+str(row[1])+"</td><td>"+str(row[2])+"</td><td>" + str(datetime.datetime.fromtimestamp(row[3] / 1000000))[
                                :str(datetime.datetime.fromtimestamp(row[3] / 1000000)).rfind(".")] + "</td><td>"+str(datetime.datetime.fromtimestamp(row[4] / 1000000))[
                                :str(datetime.datetime.fromtimestamp(row[4] / 1000000)).rfind(".")]+"</td></tr>")
    except:
        pass
    finally:
        with open("report.html", "a") as f2:
            f2.write("</tbody></table>")
        f2.close()
        f.close()
        f1.close()

def closeHTML():
    try:
        with open("report.html", "a") as f1:
            f1.write("</div></body></html>")
    except:
        pass
    finally:
        f1.close()