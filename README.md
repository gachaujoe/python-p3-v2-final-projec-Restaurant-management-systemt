# Restaurant Management System

A command-line interface (CLI) application for managing restaurant operations including customers, menu items, and orders.

## Features

- Add and manage customers
- Create and maintain menu items
- Process customer orders
- View order history
- Input validation and error handling
- Colorful interface using Colorama
- Tabulated data display using Tabulate

## Requirements

- Python 3.8+
- Pipenv for dependency management

## Installation

1. Clone the repository:

```bash
git clone git@github.com:gachaujoe/python-p3-v2-final-projec-Restaurant-management-systemt.git
cd lib
```

2. Install dependencies using Pipenv:

```bash
pipenv install
```

3. Activate the virtual environment:

```bash
pipenv shell
```

## Usage

Run the CLI application:

```bash
python cli.py
```

Follow the on-screen prompts to:

- Add new customers
- Add menu items
- Create orders
- View order history

## Testing each feature systematically

1.# Run the program
python lib/cli.py

# Choose option 1 to add a customer

# Enter test data:

Name: Joe Gachau
Email: gashjoe@gmial.com
Phone: 0722222222

2.# Choose option 2 to add a menu item

# Enter test data:

Name: Githeri special
Description: Githeri special
Price: 150
Category: Dinner

3.# Choose option 3 to create an order

# Select customer ID from displayed list

# Select menu item from displayed list

# Enter quantity

4.# Choose option 4 to view all orders

# Verify that the order appears correctly

## Project Structure

- `lib/`
  - `models/`
    - `__init__.py`: Database configuration
    - `customer.py`: Customer model
    - `menu_item.py`: MenuItem model
    - `order.py`: Order model
  - `cli.py`: Main CLI interface
  - `helpers.py`: Helper functions

## Database Schema

The application uses SQLAlchemy ORM with three related tables:

1. `customers`

   - id (Primary Key)
   - name
   - email (Unique)
   - phone

2. `menu_items`

   - id (Primary Key)
   - name
   - description
   - price
   - category

3. `orders`
   - id (Primary Key)
   - customer_id (Foreign Key)
   - menu_item_id (Foreign Key)
   - quantity
   - total_price
   - order_date

## Dependencies

- SQLAlchemy: Database ORM
- Tabulate: Pretty-print tabular data
- Colorama: Terminal text styling

## Error Handling

The application includes comprehensive error handling for:

- Invalid input validation
- Database constraints
- Resource not found
- General exceptions

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

