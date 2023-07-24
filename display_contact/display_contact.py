# prog
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import message_dialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import io
import tkinter as tk


def display_images(conn, contact_uuid):
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM images WHERE contact_uuid = ?", (contact_uuid,))
        images = cur.fetchall()
        if len(images) == 0:
            message_dialog(title="Display Contact",
                           text="No Images Available for This Contact").run()
        else:
            fig = plt.figure()

            n = len(images)
            rows = int(n ** 0.5)

            if rows ** 2 < n:
                rows += 1

            for i, contact in enumerate(images):
                img = Image.open(io.BytesIO(contact[2]))
                ax = fig.add_subplot(rows, rows, i + 1)
                ax.imshow(img)
                ax.set_title(f'Image {i + 1}')

            plt.tight_layout()
            plt.show()

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
                    "Description"]

    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM contacts WHERE uuid = ?", (contact_uuid,))
        contact = cur.fetchall()[0]

        text = ""
        for x in range(len(display_info)):
            text += display_info[x] + ": " + contact[x+1] + "\n"

        if yes_no_dialog(title="Display Contact",
                         text="Display Images?",
                         yes_text="YES",
                         no_text="NO").run():
            display_images(conn, contact_uuid)

        message_dialog(title="Display Contact",
                       text=text,
                       ok_text="OK").run()
