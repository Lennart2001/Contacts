# done
from prompt_toolkit.shortcuts import checkboxlist_dialog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import message_dialog
import os


def edit_description(conn, description_text, uuid):
    os.system("touch /Users/hacker/PycharmProjects/contacts/temp_files/cur_description.txt")
    with open("/Users/hacker/PycharmProjects/contacts/temp_files/cur_description.txt", "w") as file:
        file.write(description_text.strip('\n').replace('.\n', '. '))
        file.close()
    os.system("nano /Users/hacker/PycharmProjects/contacts/temp_files/cur_description.txt")
    text = ""
    with open("/Users/hacker/PycharmProjects/contacts/temp_files/cur_description.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            text += line
        file.close()
    os.system("rm /Users/hacker/PycharmProjects/contacts/temp_files/cur_description.txt")
    if description_text == lines:
        print("No Changes to Description - Edit Contact")
    else:
        cur = conn.cursor()
        query = "UPDATE contacts SET description = ? WHERE uuid = ?"
        values = (text, uuid)
        cur.execute(query, values)


def replace_helper(conn, title, column, value, uuid):
    cur = conn.cursor()
    text = input_dialog(title="Edit Contact",
                        text=f"Current {title}: {value}").run()
    if text is None or text == "" or text == value:
        message_dialog(title="Edit Contact",
                       text=f"*{title}* Was NOT Changed!").run()
        return False
    else:
        query = "UPDATE contacts SET " + str(column) + " = ? WHERE uuid = ?"
        values = (text.title(), uuid)
        cur.execute(query, values)
        return True


def edit_contact(conn, contact_uuid):
    if conn is not None:
        cur = conn.cursor()
        query = "SELECT * FROM contacts WHERE uuid = ?"
        cur.execute(query, (contact_uuid,))
        rows = cur.fetchall()

        description = "\n" + rows[0][21].replace('. ', '.\n')

        columns = [("first_name", f"First Name: {rows[0][1]}"),
                   ("middle_name", f"Middle Name: {rows[0][2]}"),
                   ("last_name", f"Last Name: {rows[0][3]}"),
                   ("nickname", f"Nickname: {rows[0][4]}"),
                   ("date_of_birth", f"Birthday: {rows[0][5]}"),
                   ("gender", f"Gender: {rows[0][6]}"),
                   ("ethnicity", f"Ethnicity: {rows[0][7]}"),
                   ("nationality", f"Nationality: {rows[0][8]}"),
                   ("spoken_languages", f"Spoken Languages: {rows[0][9]}"),
                   ("address", f"Address: {rows[0][10]}"),
                   ("company_email", f"Company Email: {rows[0][11]}"),
                   ("personal_email", f"Personal Email: {rows[0][12]}"),
                   ("company_phone_number", f"Company Phone Number: {rows[0][13]}"),
                   ("personal_phone_number", f"Personal Phone Number: {rows[0][14]}"),
                   ("home_phone_number", f"Home Phone Number: {rows[0][15]}"),
                   ("current_company", f"Current Company: {rows[0][16]}"),
                   ("occupation", f"Occupation: {rows[0][17]}"),
                   ("children_yes_no", f"Children (Yes/No): {rows[0][18]}"),
                   ("political_affiliation_dem_rep", f"Political Affiliation: {rows[0][19]}"),
                   ("met_where", f"Met Where: {rows[0][20]}"),
                   ("description", f"Description: {description}"),
                   ]

        results = checkboxlist_dialog(title="Edit Contact",
                                      text="Select Which You Want To Change",
                                      values=columns,
                                      ok_text="ENTER",
                                      cancel_text="CANCEL").run()

        column_dictionary = {"first_name": 1,
                             "middle_name": 2,
                             "last_name": 3,
                             "nickname": 4,
                             "date_of_birth": 5,
                             "gender": 6,
                             "ethnicity": 7,
                             "nationality": 8,
                             "spoken_languages": 9,
                             "address": 10,
                             "company_email": 11,
                             "personal_email": 12,
                             "company_phone_number": 13,
                             "personal_phone_number": 14,
                             "home_phone_number": 15,
                             "current_company": 16,
                             "occupation": 17,
                             "children_yes_no": 18,
                             "political_affiliation_dem_rep": 19,
                             "met_where": 20}

        user_info_changing_counter = []
        # This just keeps track of whether the user actually changed the info

        if results is None:
            message_dialog(title="Edit Contact",
                           text="Canceled Editing of Contact").run()
            results = []  # Makes sure that results can be read by len() function or other functions

        if len(results) == 0:
            message_dialog(title="Edit Contact",
                           text="No Changes were Made!").run()
        else:
            for result in results:
                if result == "description":
                    edit_description(conn,
                                     description_text=description,
                                     uuid=contact_uuid)

                else:
                    user_info_changing_counter.append(replace_helper(conn,
                                                                     title=result.replace("_", " ").title(),
                                                                     column=result,
                                                                     value=rows[0][column_dictionary[result]],
                                                                     uuid=contact_uuid))

            if True in user_info_changing_counter:
                conn.commit()
                message_dialog(title="Edit Contact",
                               text="Successfully Changed Contact Info").run()
            else:
                message_dialog(title="Edit Contact",
                               text="Nothing Was Changed").run()
    else:
        print("Could not CREATE CONTACT because the Connection to Database was NONE - Edit Contact")