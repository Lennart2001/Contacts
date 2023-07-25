#!/bin/bash

cd ..
DIRECTORY=$(pwd)
DATABASE_NAME="data.db"
DATABASE_PATH="${DIRECTORY}/${DATABASE_NAME}"

if [ ! -f $DATABASE_PATH ]; then
  echo "Database doesn't exist."
  echo "Creating Database now..."
  sqlite3 "$DATABASE_PATH" "CREATE TABLE contacts (
    uuid TEXT NOT NULL,
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    nickname TEXT,
    date_of_birth DATE,
    gender TEXT,
    ethnicity TEXT,
    nationality TEXT,
    spoken_languages TEXT,
    address TEXT,
    company_email TEXT,
    personal_email TEXT,
    company_phone_number TEXT,
    personal_phone_number TEXT,
    home_phone_number TEXT,
    current_company TEXT,
    occupation TEXT,
    children_yes_no TEXT,
    political_affiliation_dem_rep TEXT,
    met_where TEXT,
    description TEXT,
    contact_created TEXT,
    contact_last_edited TEXT);
    CREATE TABLE documents (
    contact_uuid TEXT NOT NULL,
    document_uuid TEXT NOT NULL,
    document BLOB NOT NULL,
    document_added TEXT NOT NULL);
    CREATE TABLE images (
    contact_uuid TEXT NOT NULL,
    image_uuid TEXT NOT NULL,
    image BLOB NOT NULL,
    image_added TEXT NOT NULL);"
else
  echo "Database already exists."
fi

