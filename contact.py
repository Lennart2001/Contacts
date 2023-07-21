class Contact:
    def __init__(self,
                 first_name=None,
                 middle_name=None,
                 last_name=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

        self.total = self.quantify()

    def quantify(self):
        complete_dict = {}

        complete_dict["First Name"] = self.first_name
        complete_dict["Middle Name"] = self.middle_name
        complete_dict["Last Name"] = self.last_name


        return complete_dict

    def update_contact(self):
        return

    def print_contact(self):
        for x in self.total:
            print(x + ":", self.total[x] if self.total[x] else "N/A")

