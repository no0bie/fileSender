import sqlite3, os, random

def resetDB():
    #os.remove("fileManager.db")
    dbConnector = sqlite3.connect("fileManager.db")
    dbMan = dbConnector.cursor()
    dbMan.execute('''CREATE TABLE fileLocation(id int, fileNames text)''')
    dbConnector.commit()
    dbConnector.close()


def writeDB(fileNames):
    dbConnector = sqlite3.connect("fileManager.db")
    dbMan = dbConnector.cursor()
    code = random.randint(999, 9999)
    while (doesExist(dbMan, code)):
        code = random.randint(999, 9999)
    dbMan.execute("INSERT INTO fileLocation VALUES ("+str(code)+",'"+fileNames+"')")
    dbConnector.commit()
    dbConnector.close()
    return code


def readDB(code):
    dbConnector = sqlite3.connect("fileManager.db")
    dbMan = dbConnector.cursor()
    read = dbMan.execute('SELECT * FROM fileLocation WHERE id='+str(code))
    print(read.fetchall())
    dbConnector.close()

def doesExist(dbManCheck, coded):
    read = dbManCheck.execute('SELECT COUNT(1) FROM fileLocation WHERE id='+str(coded))
    return read.fetchone()[0]
resetDB()