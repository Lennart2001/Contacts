# done
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.shortcuts import yes_no_dialog
import uuid
import datetime


def ask_for_info(give_me):
    while True:
        text = input_dialog(title="Create Contact",
                            text=give_me,
                            ok_text="OK",
                            cancel_text="EXIT").run()
        if text is None:
            if yes_no_dialog(title="Create Contact",
                          text="Are you sure you want to EXIT?",
                          yes_text="EXIT",
                          no_text="STAY").run():
                return None
        else:
            return text


def create_contact(conn):
    if conn is not None:
        needed_info = ["First Name",
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
                       "Description"]

        contact_uuid = str(uuid.uuid4())

        supplied_info = [contact_uuid]

        no_info_given = 0

        for info in needed_info:
            received_info = ask_for_info(info)
            if received_info is None:
                message_dialog(title="Create Contact",
                               text="You Exited Contact Creation\nContact Was Not Created").run()
                return
            if received_info == "" or received_info.upper() == "N/A":
                received_info = ""
                no_info_given += 1
            supplied_info.append(received_info.title())

        if no_info_given > 6:
            if not yes_no_dialog(title="Create Contact",
                                 text=f"Are you sure you want to create this contact?\nYou are missing {no_info_given} info slots!",
                                 yes_text="CREATE",
                                 no_text="DELETE").run():
                return

        now = str(datetime.datetime.now())
        supplied_info.append(now)
        supplied_info.append(now)

        cur = conn.cursor()
        cur.execute("INSERT INTO contacts (uuid,"
                    "first_name,"
                    "middle_name,"
                    "last_name,"
                    "nickname,"
                    "date_of_birth,"
                    "gender,"
                    "ethnicity,"
                    "nationality,"
                    "spoken_languages,"
                    "address,"
                    "company_email,"
                    "personal_email,"
                    "company_phone_number,"
                    "personal_phone_number,"
                    "home_phone_number,"
                    "current_company,"
                    "occupation,"
                    "children_yes_no,"
                    "political_affiliation_dem_rep,"
                    "met_where,"
                    "description,"
                    "contact_created,"
                    "contact_last_edited"
                    ") VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", supplied_info)

        conn.commit()

        cur.execute("SELECT * FROM contacts WHERE uuid = ?", (contact_uuid,))
        rows = cur.fetchall()

        for row in rows:
            print(row)

        message_dialog(title="Create Contact",
                       text="You Successfully Created a Contact").run()

    else:
        print("Could not CREATE CONTACT because the Connection to Database was NONE - Create Contact")


# CREATE TABLE contacts (
#     uuid TEXT NOT NULL,
#     first_name TEXT,
#     middle_name TEXT,
#     last_name TEXT,
#     nickname TEXT,
#     date_of_birth DATE,
#     gender TEXT,
#     ethnicity TEXT,
#     nationality TEXT,
#     spoken_languages TEXT,
#     address TEXT,
#     company_email TEXT,
#     personal_email TEXT,
#     company_phone_number TEXT,
#     personal_phone_number TEXT,
#     home_phone_number TEXT,
#     current_company TEXT,
#     occupation TEXT,
#     children_yes_no TEXT,
#     political_affiliation_dem_rep TEXT,
#     met_where TEXT,
#     description TEXT,
#     contact_created TEXT,
#     contact_last_edited TEXT
# );
