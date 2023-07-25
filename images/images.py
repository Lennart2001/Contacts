#prog
import io

import cv2
import numpy as np
from prompt_toolkit.shortcuts import input_dialog, message_dialog
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


def display_images(conn, contact_uuid):
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT * FROM images WHERE contact_uuid = ?", (contact_uuid,))
        images = cur.fetchall()
        if len(images) == 0:
            message_dialog(title="Display Contact",
                           text="No Images Available for This Contact").run()
        else:
            for i, contact in enumerate(images):
                cv2.namedWindow(f'Image: {i+1}', cv2.WINDOW_NORMAL)
                image = Image.open(io.BytesIO(contact[2]))
                image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

                cv2.imshow(f'Image: {i+1}', image)
                cv2.waitKey(0)
                cv2.destroyWindow(f'Image: {i+1}')

            cv2.waitKey(1)
            cv2.destroyAllWindows()
