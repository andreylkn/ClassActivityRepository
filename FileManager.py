class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def save(self, customer):
        with open(self.filename, 'a') as file:
            file.write(customer.to_string())
            file.write("-" * 40 + "\n")  # Separator line