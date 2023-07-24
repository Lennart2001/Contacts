#prog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import yes_no_dialog
import sqlite3
import os
import uuid
from PIL import Image
import matplotlib.pyplot as plt
import datetime



def convert_to_binary_data(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def show_images_from_temp_folder():
    #TODO Get the binary values from the database, based on the contact_uuid and then display each image
    # Related to that contact_uuid
    image_files = []

    # Create subplots
    fig, axs = plt.subplots(1, len(image_files))

    for i, image_file in enumerate(image_files):
        # Open an image file
        img = Image.open(image_file)
        # Display the image on the appropriate subplot
        axs[i].imshow(img)

    plt.show()


def update_database_add_image(conn, contact_uuid, binary_value):
    if conn is not None:
        cur = conn.cursor()
        cur.execute("INSERT INTO images (uuid, image) VALUES (?,?)", (contact_uuid, binary_value))
        conn.commit()


def add_images(conn, contact_uuid):
    if conn is not None:
        image_path = get_image_path()
        if image_path is not None:
            if os.path.exists(image_path):
                binary_image = convert_to_binary_data(image_path)
                cur = conn.cursor()
                cur.execute("INSERT INTO images (uuid, image) VALUES (?,?)", (contact_uuid, binary_image))
                conn.commit()
                print("Successfully Inserted Image to Database - Add Images")
            else:
                print("It appears This Image Path Does Not Exist - Add Images")
        else:
            print("Image was not Selected/Given - Add Images")
    else:
        print("Could not establish connection with Database - Add Images")

