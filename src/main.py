#done
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.shortcuts import input_dialog
from create_contact import create_contact
from search_contacts import search_contact
import sqlite3
from sqlite3 import Error
import os
import time
import subprocess


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    """
    conn = None
    try:
        if os.path.exists(db_file):
            conn = sqlite3.connect(db_file)
            print(f'Successful connection with SQLite version: {sqlite3.version}')
        else:
            print(f'No database file found at {db_file}')
    except Error as e:
        print(e)

    return conn


def check_password():
    password_texts = ["Please type your password:",
                      "Please try again:",
                      "Please try again:"]
    for x in range(3):
        result = input_dialog(
            title="Password",
            text=password_texts[x],
            password=True,
            ok_text="ENTER",
            cancel_text="TERMINATE"
        ).run()

        if result == "1234":
            return True
        elif result is None:
            return False
        time.sleep(0.1)
    return False


def select_path():
    rows = [
        ("search_contact", "Search Contact"),
        ("create_contact", "Create Contact")]
    result = radiolist_dialog(
        title="Main Menu",
        text="Select some items from the list:",
        values=rows,
        ok_text="ENTER",
        cancel_text="TERMINATE"
    ).run()

    return result


def main():

    if check_password():
        os.system("chmod +x scripts/database.sh")
        subprocess.run("scripts/database.sh")

        conn = create_connection("assets/data.db")

        if conn is not None:
            while True:

                result = select_path()

                if result is not None:

                    if result == "search_contact":
                        search_contact.search_contact(conn)
                    elif result == "create_contact":
                        create_contact.create_contact(conn)

                else:
                    conn.close()
                    print("Canceled Selection - Main Menu\n\n** Terminating Program **\n")
                    break
        else:
            print("Error! Cannot create the database connection.\n\n** Terminating Program **\n")
    else:
        print("\nAccess Denied.\n\n** Terminating Program **\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted!")
