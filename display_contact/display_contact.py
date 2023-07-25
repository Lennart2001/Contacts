# prog
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import message_dialog
from datetime import datetime

from images.images import display_images


def display_contact(conn, contact_uuid):
    display_info = ["First Name",
                    "Middle Name",
                    "Last Name",
                    "Nickname",
                    "Date of Birth (YYYY-MM-DD)",
                    "Gender",
                    "Ethnicity",
                    "Nationality",
                    "Languages Spoken",
                    "Current Address",
                    "Company Email",
                    "Personal Email",
                    "Company Phone Number",
                    "Personal Phone Number",
                    "Home Phone Number",
                    "Current Company",
                    "Occupation",
                    "Children(Yes/No)",
                    "Political Affiliation (Dem/Rep)",
                    "Met Where?",
                    "Description",
                    "Account Creation",
                    "Account Last Edited"]

    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM contacts WHERE uuid = ?", (contact_uuid,))
        contact = cur.fetchall()[0]

        text = ""
        for x in range(len(display_info)):
            if display_info[x] == "Account Last Edited" or display_info[x] == "Account Creation":
                if display_info[x] == "Account Creation":
                    text += "\n --> YYYY-MM-DD HH:MM:SS <--\n"

                time_str = datetime.strptime(contact[x + 1], "%Y-%m-%d %H:%M:%S.%f")
                text += display_info[x] + ": " + \
                        str(time_str.date()) + " " + \
                        str(time_str.hour) + ":" + \
                        str(time_str.minute) + ":" + \
                        str(time_str.second) + "\n"
            else:
                text += display_info[x] + ": " + contact[x + 1] + "\n"

        if yes_no_dialog(title="Display Contact",
                         text="Display Images?",
                         yes_text="YES",
                         no_text="NO").run():
            display_images(conn, contact_uuid)

        message_dialog(title="Display Contact",
                       text=text,
                       ok_text="OK").run()
