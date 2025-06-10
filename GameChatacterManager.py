import sqlite3

db = sqlite3.connect('characters.db')

cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    level INTEGER DEFAULT '0',
    health INTEGER DEFAULT '100'
);
""")

db.commit()


def getString(message):
    string = None
    while string == None or string == '':
        string = input(f"{message}\n")
    return string


def getInteger(message):
    number = None
    while number == None:
        number = input(f"{message}\n")
        try:
            number = int(number)
            if isinstance(number, int):
                return number
        except ValueError:
            number = None
        

#the main menu allowing selection of what you might want to do
def main():
    choice = int(input("""
1. Create New Character
2. View All Characters
3. Search For Character
4. Update Character
5. Delete Character
6. Exit
"""))
    if choice == 1:
        createNewCharacter()
    elif choice == 2:
        veiwCharacters()
    elif choice == 3:
        searchCharacter()
    elif choice == 4:
        CharacterId = getInteger("What is your characters id")
        updateCharacter(CharacterId)
    elif choice == 5:
        CharacterId = getInteger("What is your characters id")
        deleteCharacter(CharacterId)
    elif choice == 6:
        exit()
    else:
        print("Invalid Choice")
        main()

#allows the creation of a character to the database
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

#allows the viewing of all characters
def veiwCharacters():
    cur.execute('SELECT * FROM characters')
    data = cur.fetchall()
    for line in data:
        print(line)
    main()

#allows searching of a character based upon their attributes
def searchCharacter():
    choice = int(input("""
1. Search For Character by ID
2. Search For Character by Name
3. Search For Character by Class
4. Search For Character by Level
5. Search For Character by Health
"""))
    if choice == 1:
        characterID = getInteger("What is the id of the characters you want to search for")
        cur.execute("SELECT * FROM characters WHERE id = ? ", [characterID])
        characters = cur.fetchall()
        for character in characters:
            print(character)

    elif choice == 2:
        characterName = getString("What is the name of the characters you want to search for")
        cur.execute("SELECT * FROM characters WHERE name = ? ", [characterName])
        characters = cur.fetchall()
        for character in characters:
            print(character)

    elif choice == 3:
        characterClass = getString("What is the class of the characters you want to search for")
        cur.execute("SELECT * FROM characters WHERE class = ? ", [characterClass])
        characters = cur.fetchall()
        for character in characters:
            print(character)

    elif choice == 4:
        characterLevel = getString("What is the level of the characters you want to search for")
        cur.execute("SELECT * FROM characters WHERE class = ? ", [characterLevel])
        characters = cur.fetchall()
        for character in characters:
            print(character)

    elif choice == 5:
        characterHealth = getString("What is the health of the characters you want to search for")
        cur.execute("SELECT * FROM characters WHERE health = ? ", [characterHealth])
        characters = cur.fetchall()
        for character in characters:
            print(character)
    main()

#can update one of te characters attributes if characters id is specified
def updateCharacter(CharacterId):
    choice = int(input("""
1. Edit Name
2. Edit Class
3. Edit Level
4. Edit Health
"""))
    if choice == 1:
        newCharacterName = getString("What do you want to change the characters name to")
        cur.execute("""
                    UPDATE characters
                    SET name = ?
                    WHERE id = ?
                    """, (newCharacterName, CharacterId))
        db.commit()
        IdUsed = cur.lastrowid
        print(f"Updated Characters Name with a id of {IdUsed}")

    elif choice == 2:
        newClassName = getString("What do you want to change the characters class to")
        cur.execute("""
                    UPDATE characters
                    SET class = ?
                    WHERE id = ?
                    """, (newClassName, CharacterId))
        db.commit()
        IdUsed = cur.lastrowid
        print(f"Updated Characters Class with a id of {IdUsed}")

    elif choice == 3:
        newLevel = getInteger("What do you want to change the characters level to")
        cur.execute("""
                    UPDATE characters
                    SET level = ?
                    WHERE id = ?
                    """, (newLevel, CharacterId))
        db.commit()
        IdUsed = cur.lastrowid
        print(f"Updated Characters Level with a id of {IdUsed}")

    elif choice == 4:
        newHealth = getInteger("What do you want to change the characters health to")
        cur.execute("""
                    UPDATE characters
                    SET health = ?
                    WHERE id = ?
                    """, (newHealth, CharacterId))
        db.commit()
        IdUsed = cur.lastrowid
        print(f"Updated Characters Health with a id of {IdUsed}")
    main()

#deletes a character from the database from the user providing the characters id
def deleteCharacter(CharacterId):
    cur.execute("""
                DELETE FROM characters
                WHERE id = ?
                """, [CharacterId])
    db.commit()
    print(f"Deleted Character with a id of {CharacterId}")
    main()

def exit():
    print("Just Kill It")

main()
