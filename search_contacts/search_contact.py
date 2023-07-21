# done
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.shortcuts import message_dialog
from selected_contact.selected import show_contact_options


def first_name_search(conn):
    if conn is not None:
        text = input_dialog(title="Search BY First Name",
                            text="Type the First (or partial) Name:",
                            cancel_text="BACK").run()

        if text is not None:
            cur = conn.cursor()
            query = "SELECT uuid, first_name, last_name, date_of_birth, address FROM contacts WHERE first_name LIKE ? " \
                    "ORDER BY first_name ASC, last_name ASC LIMIT 50"
            cur.execute(query, [f"{text}%"])
            return cur.fetchall()
        else:
            print("Canceled Selection - Name Search")
            return None


def last_name_search(conn):
    if conn is not None:
        text = input_dialog(title="Search BY Last Name",
                            text="Type the Last (or partial) Name:",
                            cancel_text="BACK").run()

        if text is not None:
            cur = conn.cursor()
            query = "SELECT uuid, first_name, last_name, date_of_birth, address FROM contacts WHERE last_name LIKE ? ORDER " \
                    "BY first_name ASC, last_name ASC LIMIT 50"
            cur.execute(query, [f"{text}%"])
            return cur.fetchall()
        else:
            print("Canceled Selection - Name Search")
            return None


def first_and_last_name_search(conn):
    if conn is not None:
        text_1 = input_dialog(title="Search BY Both Names",
                              text="Type the First (or partial) Name:",
                              cancel_text="BACK").run()

        text_2 = input_dialog(title="Search BY Both Names",
                              text="Type the Last (or partial) Name:",
                              cancel_text="BACK").run()

        if text_1 is not None and text_2 is not None:
            cur = conn.cursor()
            query = "SELECT uuid, first_name, last_name, date_of_birth, address FROM contacts WHERE first_name LIKE ? AND " \
                    "last_name LIKE ? ORDER BY first_name ASC, last_name ASC LIMIT 50"
            cur.execute(query, [f"{text_1}%", f"{text_2}%"])
            return cur.fetchall()
        else:
            print("Canceled Selection - Name Search")
            return None


def name_search(conn, rows):
    while True:
        if conn is not None:

            display_rows = []
            full_name_list = {}

            for row in rows:
                display_rows.append((str(row[0]), str(row[1] + " " + row[2] + ", " + row[3] + ", " + row[4])))
                full_name_list[row[0]] = str(row[1] + " " + row[2])

            if len(display_rows) > 0:
                result = radiolist_dialog(
                    title="Contact Selection",
                    text="Select Your Current Contact",
                    values=display_rows,
                    ok_text="ENTER",
                    cancel_text="BACK").run()

                if result is not None:
                    show_contact_options(conn, result, full_name_list[result])
                else:
                    print("Canceled Selection - Name Search")
                break
            else:
                message_dialog(title="Contact Selection",
                               text="We Could Not Find Any Contacts").run()
                break

        else:
            print("Name Search - Error! Cannot create the database connection.\n\n** Terminating Program **\n")
            break


def search_contact(conn):
    result = radiolist_dialog(
        title="First/Last Name Search",
        text="Select some items from the list:",
        values=[("first_name", "First Name"),
                ("last_name", "Last Name"),
                ("both", "First And Last Name")],
        ok_text="ENTER",
        cancel_text="BACK").run()

    if result is not None:

        if result == "first_name":

            rows = first_name_search(conn)
            if rows is None:
                return

        elif result == "last_name":

            rows = last_name_search(conn)
            if rows is None:
                return

        elif result == "both":

            rows = first_and_last_name_search(conn)
            if rows is None:
                return

        else:
            print("Name Search - Did not select a SEARCH\n")
            return

        name_search(conn, rows)

    else:
        print("Canceled Selection - Search Contact")

