# Create class(es) in a retail industry to get information from customer and save it in a file or in a database.
from Customer import Customer
from FileManager import FileManager

def create_customer():
    print("Please enter the following information:")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")
    return Customer(name, email, phone, address)

def save_to_file(self, customer):
    with open(self.filename, 'a') as file:
        file.write(customer.to_string())
        file.write("-" * 40 + "\n")  # Separator line

def main():
    file_manager = FileManager("customers.txt")
    customer = create_customer()
    file_manager.save(customer)
    print("Customer information saved to file.")

if __name__ == "__main__":
    main()


