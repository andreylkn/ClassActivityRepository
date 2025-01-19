# Create class(es) in a retail industry to get information from customer and save it in a file or in a database.
from Classes.Customer import Customer
from Classes.FileManager import FileManager
from printing_utils import print_file_saved_message, print_getting_information_message

def create_customer():
    print_getting_information_message()
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")
    return Customer(name, email, phone, address)

def main():
    file_manager = FileManager("customers.txt")
    customer = create_customer()
    file_manager.save(customer)
    print_file_saved_message()

if __name__ == "__main__":
    main()