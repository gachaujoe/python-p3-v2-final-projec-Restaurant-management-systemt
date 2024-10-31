# lib/cli.py

# from helpers import (
#     exit_program,
#     helper_1
# )


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             helper_1()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Some useful function")


# if __name__ == "__main__":
#     main()


from helpers import (
    add_customer,
    add_menu_item,
    create_order,
    view_orders,
    exit_program
)
from colorama import init, Fore, Style
from models.base import Base
from models.session import engine


Base.metadata.create_all(engine)

init()

def main():
    print(Fore.GREEN + "\nWelcome to Restaurant Management System!" + Style.RESET_ALL)
    
    while True:
        menu()
        choice = input(Fore.CYAN + "\nEnter your choice (0-5): " + Style.RESET_ALL)
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_customer()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            create_order()
        elif choice == "4":
            view_orders()
        else:
            print(Fore.RED + "Invalid choice! Please try again." + Style.RESET_ALL)

def menu():
    """Display the main menu"""
    print("\nPlease select an option:")
    print("1. Add New Customer")
    print("2. Add New Menu Item")
    print("3. Create New Order")
    print("4. View All Orders")
    print("0. Exit")

if __name__ == "__main__":
    main()