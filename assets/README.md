## CONTACTS TABLE
- **UUID**: A unique identifier assigned to each contact. This is a randomly generated string that ensures each contact has a unique identifier, regardless of any shared information such as name or email address.
- **First Name**: The given name of an individual, typically assigned at birth.
- **Middle Name**: A secondary name given to an individual, positioned between their first and last name.
- **Last Name**: The surname or family name of an individual.
- **Nickname**: A familiar, informal name used in place of the full name of an individual.
- **Date of Birth**: The specific day, month, and year an individual was born.
- **Gender**: The identity an individual aligns with in terms of masculinity, femininity, or otherwise.
- **Ethnicity**: The ethnic group or groups an individual identifies with, often based on shared cultural heritage, ancestry, or history.
- **Nationality**: The country or countries an individual holds citizenship in.
- **Languages Spoken**: The language or languages an individual can communicate in.
- **Current Address**: The physical location where an individual currently resides.
- **Company Email**: The official email address provided to an individual by their employer for professional communication.
- **Personal Email**: The private email address used by an individual for non-professional communication.
- **Company Phone Number**: The official phone number provided to an individual by their employer, often for professional purposes.
- **Personal Phone Number**: The private phone number owned by an individual for personal communication.
- **Home Phone Number**: The landline number associated with an individual's place of residence.
- **Current Company**: The company or organization where an individual is currently employed.
- **Occupation**: The specific role or job an individual performs at their place of employment.
- **Children (Yes/No)**: A simple yes or no indicating whether an individual has children.
- **Political Affiliation (Dem/Rep)**: An individual's association with a particular political party, such as the Democratic or Republican party in the United States.
- **Met Where?**: The location or context in which you first met or made contact with this individual.
- **Description**: A brief summary or profile describing the individual, potentially including personal characteristics, interests, and professional background.
- **Contact Created**: The date when this individual's contact information was first added or created in your system or database.
- **Contact Last Edited**: The most recent date when this individual's contact information was updated or edited in your system or database.

## IMAGES TABLE
- **contact_uuid**: The unique identifier of the contact to which the image belongs. This matches the UUID in the Contacts table.
- **image_uuid**: A unique identifier assigned to each image. This is a randomly generated string that ensures each image has a unique identifier.
- **image**: The binary data of the image. This is stored as a BLOB (Binary Large OBject) in the SQLite database.
- **image_added**: The date when the image was first added to the database.