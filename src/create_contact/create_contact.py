# done
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.shortcuts import yes_no_dialog
import uuid
import datetime
import os
from images.images import convert_to_binary_data


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


def add_images(conn, contact_uuid):
    if conn is not None:
        changed_contact = False
        cur = conn.cursor()
        while True:
            image_path = input_dialog(title="Create Contact",
                                      text="Please give the image Path:",
                                      ok_text="ENTER",
                                      cancel_text="CANCEL").run()
            if image_path is not None and os.path.exists(image_path.strip(" ")):
                image_data = convert_to_binary_data(image_path.strip(" "))
                image_uuid = str(uuid.uuid4())
                now = str(datetime.datetime.now())
                cur.execute("INSERT INTO images (contact_uuid, image_uuid, image, image_added) VALUES (?,?,?,?)",
                            (contact_uuid, image_uuid, image_data, now))

                print("You successfully Added an Image - Create Contact")
                changed_contact = True
            else:
                message_dialog(title="Add Image",
                               text="You did not provide a Proper Image Path",
                               ok_text="OK").run()

                print("User did not provide a Proper Image Path - Create Contact")

            if not yes_no_dialog(title="Create Contact",
                                 text="Would You Like to Add an(other) Image to This Contact?",
                                 yes_text="YES",
                                 no_text="NO").run():
                break
        conn.commit()
        return changed_contact


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

        cur = conn.cursor()

        add_images(conn, contact_uuid)

        if no_info_given > 6:
            if not yes_no_dialog(title="Create Contact",
                                 text=f"Are you sure you want to create this contact?\nYou are missing {no_info_given} info slots!",
                                 yes_text="CREATE",
                                 no_text="DELETE").run():
                conn.rollback()
                return

        now = str(datetime.datetime.now())
        supplied_info.append(now)
        supplied_info.append(now)

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


        # # Kind of unnessary - Because the user won't really see this
        # cur.execute("SELECT * FROM contacts WHERE uuid = ?", (contact_uuid,))
        # rows = cur.fetchall()
        #
        # for row in rows:
        #     print(row)

        message_dialog(title="Create Contact",
                       text="You Successfully Created a Contact").run()

    else:
        print("Could not CREATE CONTACT because the Connection to Database was NONE - Create Contact")

