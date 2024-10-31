# # lib/helpers.py

# def helper_1():
#     print("Performing useful function#1.")


# def exit_program():
#     print("Goodbye!")
#     exit()

from models import session, Customer, MenuItem, Order
from tabulate import tabulate
from colorama import Fore, Style
import re

def validate_email(email):
    """Validate email format using regex"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number format"""
    pattern = r'^\d{10}$'
    return re.match(pattern, phone) is not None

def add_customer():
    """Add a new customer to the database"""
    print(Fore.CYAN + "\nAdding New Customer" + Style.RESET_ALL)
    
    name = input("Enter customer name: ").strip()
    while not name:
        print(Fore.RED + "Name cannot be empty!" + Style.RESET_ALL)
        name = input("Enter customer name: ").strip()
    
    email = input("Enter customer email: ").strip()
    while not validate_email(email):
        print(Fore.RED + "Invalid email format!" + Style.RESET_ALL)
        email = input("Enter customer email: ").strip()
    
    phone = input("Enter customer phone (10 digits): ").strip()
    while not validate_phone(phone):
        print(Fore.RED + "Invalid phone format! Please enter 10 digits." + Style.RESET_ALL)
        phone = input("Enter customer phone (10 digits): ").strip()
    
    try:
        customer = Customer(name=name, email=email, phone=phone)
        session.add(customer)
        session.commit()
        print(Fore.GREEN + "\nCustomer added successfully!" + Style.RESET_ALL)
    except Exception as e:
        session.rollback()
        print(Fore.RED + f"\nError adding customer: {str(e)}" + Style.RESET_ALL)

def add_menu_item():
    """Add a new menu item to the database"""
    print(Fore.CYAN + "\nAdding New Menu Item" + Style.RESET_ALL)
    
    name = input("Enter item name: ").strip()
    while not name:
        print(Fore.RED + "Name cannot be empty!" + Style.RESET_ALL)
        name = input("Enter item name: ").strip()
    
    description = input("Enter item description: ").strip()
    
    while True:
        try:
            price = float(input("Enter item price: ").strip())
            if price <= 0:
                raise ValueError
            break
        except ValueError:
            print(Fore.RED + "Please enter a valid positive number!" + Style.RESET_ALL)
    
    category = input("Enter item category: ").strip()
    while not category:
        print(Fore.RED + "Category cannot be empty!" + Style.RESET_ALL)
        category = input("Enter item category: ").strip()
    
    try:
        menu_item = MenuItem(name=name, description=description, price=price, category=category)
        session.add(menu_item)
        session.commit()
        print(Fore.GREEN + "\nMenu item added successfully!" + Style.RESET_ALL)
    except Exception as e:
        session.rollback()
        print(Fore.RED + f"\nError adding menu item: {str(e)}" + Style.RESET_ALL)

def create_order():
    """Create a new order"""
    print(Fore.CYAN + "\nCreating New Order" + Style.RESET_ALL)
    
    # Show available customers
    customers = session.query(Customer).all()
    if not customers:
        print(Fore.RED + "No customers found! Please add a customer first." + Style.RESET_ALL)
        return
    
    customer_data = [[c.id, c.name, c.email] for c in customers]
    print("\nAvailable Customers:")
    print(tabulate(customer_data, headers=['ID', 'Name', 'Email'], tablefmt='grid'))
    
    # Get customer ID
    while True:
        try:
            customer_id = int(input("Enter customer ID: ").strip())
            customer = session.query(Customer).filter_by(id=customer_id).first()
            if customer:
                break
            print(Fore.RED + "Customer not found!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid number!" + Style.RESET_ALL)
    
    # Show available menu items
    menu_items = session.query(MenuItem).all()
    if not menu_items:
        print(Fore.RED + "No menu items found! Please add menu items first." + Style.RESET_ALL)
        return
    
    menu_data = [[i.id, i.name, i.description, i.price, i.category] for i in menu_items]
    print("\nAvailable Menu Items:")
    print(tabulate(menu_data, headers=['ID', 'Name', 'Description', 'Price', 'Category'], tablefmt='grid'))
    
    # Get menu item ID and quantity
    while True:
        try:
            item_id = int(input("Enter menu item ID: ").strip())
            menu_item = session.query(MenuItem).filter_by(id=item_id).first()
            if menu_item:
                break
            print(Fore.RED + "Menu item not found!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid number!" + Style.RESET_ALL)
    
    while True:
        try:
            quantity = int(input("Enter quantity: ").strip())
            if quantity > 0:
                break
            print(Fore.RED + "Quantity must be positive!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid number!" + Style.RESET_ALL)
    
    # Calculate total price
    total_price = menu_item.price * quantity
    
    try:
        order = Order(
            customer_id=customer_id,
            menu_item_id=item_id,
            quantity=quantity,
            total_price=total_price
        )
        session.add(order)
        session.commit()
        print(Fore.GREEN + f"\nOrder created successfully! Total price: ${total_price:.2f}" + Style.RESET_ALL)
    except Exception as e:
        session.rollback()
        print(Fore.RED + f"\nError creating order: {str(e)}" + Style.RESET_ALL)

def view_orders():
    """View all orders"""
    orders = session.query(Order).all()
    if not orders:
        print(Fore.YELLOW + "\nNo orders found!" + Style.RESET_ALL)
        return
    
    order_data = [
        [o.id, o.customer.name, o.menu_item.name, o.quantity, 
         f"${o.total_price:.2f}", o.order_date.strftime("%Y-%m-%d %H:%M:%S")]
        for o in orders
    ]
    
    print("\nAll Orders:")
    print(tabulate(order_data, 
                  headers=['ID', 'Customer', 'Item', 'Quantity', 'Total', 'Date'],
                  tablefmt='grid'))

def exit_program():
    """Exit the program"""
    print(Fore.YELLOW + "\nThank you for using Restaurant Management System. Goodbye!" + Style.RESET_ALL)
    exit()