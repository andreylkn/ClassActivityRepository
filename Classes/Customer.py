class Customer:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def to_string(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}\n"