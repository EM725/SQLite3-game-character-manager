import sqlite3

db = sqlite3.connect('example.db')

cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    level INTEGER DEFAULT '0'
);
""")

db.commit()

def main():
    choice = int(input("""
1. Create New Character
"""))
    if choice == 1:
        createNewCharacter(nm, cl)

def createNewCharacter(nm, cl):
    pass

def veiwCharacters():
    pass

def updateCharacter(i):
    pass

def deleteCharacter(i):
    pass

def exit():
    print("Just Kill it")
