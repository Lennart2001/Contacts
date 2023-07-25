#done
from datetime import datetime, timedelta
import uuid
import sqlite3
from sqlite3 import Error
import os
from faker import Faker


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    """
    conn = None
    try:
        if os.path.exists(db_file):
            conn = sqlite3.connect(db_file)
            print(f'Successful connection with SQLite version: {sqlite3.version}')
        else:
            print(f'No database file found at {db_file}')
    except Error as e:
        print(e)

    return conn


def insert_into_database(test):
    conn = create_connection("../../assets/data.db")

    for x in range(10000):
        if x % 100 == 0:
            print(str(x) + "/50000")
        birthday = datetime(1940, 1, 1) + timedelta(days=x,)
        random_uuid = uuid.uuid4()

        fake = Faker()

        new_row = (str(random_uuid),
                   fake.first_name(),
                   fake.last_name(),
                   str(birthday.date()),
                   str(fake.address()).replace("\n", ", "),
                   fake.phone_number(),
                   fake.ascii_company_email(),
                   fake.ascii_email(),
                   fake.job(),
                   fake.company(),
                   fake.ssn(),
                   fake.paragraph(nb_sentences=(x % 5) + 1))

        # if test:
        #     print(new_row)
        #
        #     if x > 10:
        #         break
        # else:
        cur = conn.cursor()
        cur.execute("INSERT INTO contacts (uuid, first_name, last_name, birthday, address, phone_number, "
                    "company_email, regular_email, job, company, ssn, description) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    new_row)

    conn.commit()


insert_into_database(False)

# CREATE TABLE contacts (
# uuid TEXT NOT NULL,
# first_name TEXT,
# last_name TEXT,
# birthday DATE,
# address TEXT,
# phone_number TEXT,
# company_email TEXT,
# regular_email TEXT,
# job TEXT,
# company TEXT,
# ssn TEXT,
# description TEXT);