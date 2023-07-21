#prog
from prompt_toolkit.shortcuts import input_dialog
import sqlite3
import os

def convert_to_binary_data(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data


def get_image_path():
    text = input_dialog(title="Image Path",
                        text="Please Drag the Image Here:").run()
    return text

def update_database_add_image(conn, contact_uuid, binary_value):
    if conn is not None:
        cur = conn.cursor()
        cur.execute("UPDATE contacts WHERE uuid = ?")


def add_images(conn):
        image_path = get_image_path()

        if image_path is not None:
            if os.path.exists(image_path):
                binary_image = convert_to_binary_data(image_path)
            else:
                print("It appears This Path Doesnt Exist - Add Images")
