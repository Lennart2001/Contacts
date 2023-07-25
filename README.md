# Contacts
A lightweight, command-line software, which allows for the creation and organizing of contacts.
We utilize SQLite3, which allows us to store images and contact information.

## Description

This software provides a simple and efficient way to manage your contacts. You can add, view, search, edit, and delete contacts.
Each contact's information, including their name, phone number, email, and optional images, are stored in an SQLite database, ensuring fast access and easy management.

## Table of Contents

1. [Installations](#installations)
2. [Usage](#usage)
3. [Database Structure and Performance](#database-structure-and-performance)
4. [License](#license)
5. [FAQs](#faqs)
6. [Contributing](#contributing)
7. [Troubleshooting and Support](#troubleshooting-and-support)

## Installations

1. Ensure Python 3.7+ is installed on your system.
2. Clone the repository to your local system.
3. Navigate to the 'src' directory of the project in your terminal.
4. Run `python3 main.py` to start the application.

## Usage

The application offers a straightforward command-line interface, making it easy to manage your contacts. To start, navigate to the 'src' directory in your terminal and run the command `python3 main.py`. This will launch the application and display the main menu with the following options:

1. **Search Contacts**: Use this option to look up a specific contact by name. After the search, you can:
   - **Edit Contact**: Modify the details of the selected contact.
   - **View Contact**: Display the full details of the selected contact.
   - **Delete Contact**: Remove the selected contact from the database.
   
2. **Create Contact**: Use this option to add a new contact to your database. You'll be guided through a series of prompts to provide information about the contact, such as name, phone number, and email. At the end, you'll have the option to add one or more images to the contact.

## Database Structure and Performance

The database used in this application is designed to efficiently store and retrieve large amounts of data. Using SQLite allows us to leverage the power of SQL queries for data management, ensuring that even with large amounts of contacts, the performance remains optimal.

When you search for a contact by name, the application performs a case-insensitive search of the database and returns all matches. However, to prevent overwhelming amounts of data from being displayed at once and to maintain a clean and user-friendly interface, only the top 50 results are shown. If the contact you're looking for isn't in these results, you may need to refine your search.

## License

This project is licensed under the MIT License. 

## FAQs

- **Q: How do I add an image to a contact?**
  A: When adding a contact, you will be prompted to provide an image. You can enter the path to the image file on your system.

- **Q: Can I search for contacts by email or phone number?**
  A: Currently, the application only supports searching for contacts by name.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue on this GitHub repository. Go crazy.

## Troubleshooting and Support

If you encounter any issues while using this software, please open an issue on this GitHub repository. Provide as much detail as possible about the issue, including the steps to reproduce it and any error messages you received.

For general queries or suggestions, you can also reach out via the issues on this repository.
