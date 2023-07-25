#prog
from prompt_toolkit.shortcuts import radiolist_dialog
from edit_contact.edit_contact import edit_contact
from display_contact.display_contact import display_contact
from delete_contact.delete_contact import delete_contact


def show_contact_options(conn, contact_uuid, full_name):
    result = radiolist_dialog(
        title="Selected Contact",
        text=f"What Would You Like to Do With Contact:\n{full_name}",
        values=[("edit", "Edit Contact"),
                ("display", "Display Contact"),
                ("delete", "Delete Contact")],
        ok_text="ENTER",
        cancel_text="BACK"
    ).run()

    if result == "edit":
        edit_contact(conn, contact_uuid)
    elif result == "display":
        display_contact(conn, contact_uuid)
    elif result == "delete":
        delete_contact(conn, contact_uuid)
    else:
        print("Canceled Selection - Show Contact Options\n\n** Terminating Program **\n")

