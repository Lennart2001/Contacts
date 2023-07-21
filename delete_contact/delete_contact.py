# done
from prompt_toolkit.shortcuts import yes_no_dialog


def delete_contact(conn, contact_uuid):
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT first_name, last_name, date_of_birth, address FROM contacts WHERE uuid = ?",
                    (contact_uuid,))
        rows = cur.fetchone()

        result = yes_no_dialog(title="Create Contact",
                               text=f"Are you sure you want to DELETE:\n{rows[0]} {rows[1]}, {rows[2]}, {rows[3]}",
                               yes_text="DELETE",
                               no_text="CANCEL").run()
        if result:
            cur.execute("DELETE FROM contacts WHERE uuid = ?", (contact_uuid,))
            conn.commit()

            print("Successfully Deleted Contact From Database - Delete Contact")
        else:
            print("Contact was NOT Deleted - Delete Contact")
    else:
        print("Could not CREATE CONTACT because the Connection to Database was NONE - Delete Contact")