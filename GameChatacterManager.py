import sqlite3

db = sqlite3.connect('example.db')

cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    level INTEGER DEFAULT '0'
    health INTEGER DEFUALT '100'
);
""")

db.commit()

def getString(message):
    string = None
    while string == None:
        string = str(input(f"{message}\n"))
    return string

def getInteger(message):
    number = None
    while number == None:
        number = int(input(f"{message}"))
    return number

def main():
    choice = int(input("""
1. Create New Character
2. View All Characters
3. Update Character
4. Delete Character
5. Exit
"""))
    if choice == 1:
        createNewCharacter()
    elif choice == 2:
        veiwCharacters()
    elif choice == 3:
        id = getInteger("What is your characters id")
        updateCharacter(id)
    elif choice == 4:
        id = getInteger("What is your characters id")
        deleteCharacter(id)
    elif choice == 5:
        exit()
    else:
        print("Invalid Choice")
        main()

def createNewCharacter():
    characterName = getString("What do you want the characters name to be")
    characterClass = getString("What do you want the characters class to be")
    cur.execute("""
                INSERT INTO characters (name, class)
                VALUES
                    (?, ?)
                """, (characterName, characterClass))
    db.commit()
    new_id = cur.lastrowid
    print(f"Created New Character with a id of {new_id}")
    main()


def veiwCharacters():
    cur.execute('SELECT * FROM characters')
    data = cur.fetchall()
    for line in data:
        print(line)


def updateCharacter(id):
    choice = int(input("""
1. Edit Name
2. Edit Class
3. Edit Level
"""))
    if choice == 1:
        newCharacterName = getString("What do you want to change the characters name to")
        cur.execute("""
                    UPDATE characters
                    SET name = ?
                    WHERE id = ?
                    """, (newCharacterName, id))
        db.commit()
        new_id = cur.lastrowid
        print(f"Updated Characters Name with a id of {new_id}")

    elif choice == 2:
        newClassName = getString("What do you want to change the characters class to")
        cur.execute("""
                    UPDATE characters
                    SET class = ?
                    WHERE id = ?
                    """, (newClassName, id))
        db.commit()
        new_id = cur.lastrowid
        print(f"Updated Characters Class with a id of {new_id}")

    elif choice == 3:
        newLevel = getInteger("What do you want to change the characters level to")
        cur.execute("""
                    UPDATE characters
                    SET level = ?
                    WHERE id = ?
                    """, (newLevel, id))
        db.commit()
        new_id = cur.lastrowid
        print(f"Updated Characters Level with a id of {new_id}")
    main()


def deleteCharacter(id):
    cur.execute("""
                DELETE FROM example
                WHERE id = ?
                """, (id))
    db.commit()
    new_id = cur.lastrowid
    print(f"Deleted Character with a id of {new_id}")

def exit():
    print("Just Kill It")
