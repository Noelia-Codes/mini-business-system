from datetime import date
inventory = {
    "tshirt basic black": {
        "price": 12.99,
        "stock": 20,
        "sold_quantity": 0,
        "category": "t-shirts",
        "supplier": "urban wear co"
    },
    "jeans slim blue": {
        "price": 39.99,
        "stock": 15,
        "sold_quantity": 0,
        "category": "jeans",
        "supplier": "denim lab"
    },
    "hoodie grey": {
        "price": 29.99,
        "stock": 10,
        "sold_quantity": 0,
        "category": "hoodies",
        "supplier": "street style inc"
    }
}
sales_log = [
    {
        "product": "tshirt basic black",
        "quantity": 2,
        "total": 25.98,
        "date": "10/05/2026"
    },
    {
        "product": "jeans slim blue",
        "quantity": 1,
        "total": 39.99,
        "date": "11/05/2026"
    },
    {
        "product": "hoodie grey",
        "quantity": 1,
        "total": 29.99,
        "date": "12/05/2026"
    },
    {
        "product": "tshirt basic black",
        "quantity": 3,
        "total": 38.97,
        "date": "13/05/2026"
    },
    {
        "product": "jeans slim blue",
        "quantity": 2,
        "total": 79.98,
        "date": "14/05/2026"
    }
]
menu = ["Inventory System:", "1. Add Product", "2. Sell Product", "3. View Inventory", "4. Sales Summary", "5. Exit"]
#Have to add something for the user to be able to cancel and go back.
def add_product():
    product_name = input("Product to add:" ).strip().lower()
    if product_name in inventory:
        decision = input(f"{product_name} already exists. Update stock? Yes/No:" ).strip().lower()
        while decision != "yes" and decision != "no":
          decision = input("Please enter yes or no:" ).strip().lower()
        if decision == "yes":
            new_stock = validate_int()
            inventory[product_name]["stock"] += new_stock
            print("Stock updated")
            print(inventory[product_name])
        else:
            print("No changes made. Back to the main menu")
    else:
      price = validate_float()
      stock = validate_int()
      sold_quantity = 0
      category = validate_text("Product Category:")
      supplier = validate_text("Product Supplier:")
      inventory[product_name] = {
              "price": price,
              "stock": stock,
              "sold_quantity": sold_quantity,
              "category": category,
              "supplier": supplier,
      }
      print("Product added to inventory!")
#add partial sell later and go back to ask product if name doesnt exist and/or cancel
def sell_product():
    product_name = input("Product name:" ).strip().lower()
    if product_name not in inventory:
        print("Product not found.")
    else:
        number = validate_int()
        stock = inventory[product_name]["stock"]
        price = inventory[product_name]["price"]
        sold_quantity = inventory[product_name]["sold_quantity"]
        sale_date = date.today()
        sale_date_formatted = sale_date.strftime("%d/%m/%Y")
        if number <= stock:
            inventory[product_name]["stock"] = stock - number
            inventory[product_name]["sold_quantity"] = sold_quantity + number
            total_price = price * number
            sales_log.append({"product": product_name, "quantity": number,
            "total": total_price, "date": sale_date_formatted})
            print("Sell added to sales log")
        else:
            print("Not enough stock")
def view_inventory():
    user_choice = input("Insert 1 to view the whole inventory or 2 to view one product:").strip()
    while user_choice != "1" and user_choice != "2":
        user_choice = input("Please enter a valid option: ").strip()
    if user_choice == "1":
        for product in inventory:
            info = f"{product}\nPrice: {inventory[product]['price']}\nStock: {inventory[product]['stock']}\nSold Quantity: {inventory[product]['sold_quantity']}\nCategory: {inventory[product]['category']}\nSupplier: {inventory[product]['supplier']}"
            print(info)
    elif user_choice == "2":
        product_name = input("Insert product name: ").strip().lower()
        if product_name in inventory:
            info = f"{product_name}\nPrice: {inventory[product_name]['price']}\nStock: {inventory[product_name]['stock']}\nSold Quantity: {inventory[product_name]['sold_quantity']}\nCategory: {inventory[product_name]['category']}\nSupplier: {inventory[product_name]['supplier']}"
            print(info)
        else:
            print("Product not found")
def sales_summary():
    total_quantity = 0
    total_revenue = 0
    for sale in sales_log:
        total_quantity += sale["quantity"]
        total_revenue += sale["total"]
    total_revenue = round(total_revenue, 2)
    info = f"Total Revenue: {total_revenue}\nTotal Sold Quantity: {total_quantity}"
    print(info)
def validate_int():
    while True:
        number = input("Insert quantity:" )
        try:
            number = int(number)
            return number
        except ValueError:
            print("Please enter a valid number")
def validate_float():
    while True:
        number = input("Insert price:" )
        try:
            number = float(number)
            return number
        except ValueError:
            print("Please enter a valid number, using dots as decimal separator")
def validate_text(message):
    while True:
        text = input(f"{message}")
        if text == "":
            print("This info is mandatory.")
        else:
            text = text.strip().lower()
            return text
#add validate for menu number
def main():
    while True:
        print("=" * 30)
        print("Inventory System".center(30))
        print("=" * 30)
        print()
        for item in menu:
            print(item)
        print()
        print("=" * 30)
        print()
        user_choice = input("What would you like to do?: ")
        try:
            user_choice = int(user_choice)
            if user_choice == 1:
                add_product()
            elif user_choice == 2:
                sell_product()
            elif user_choice == 3:
                view_inventory()
            elif user_choice == 4:
                sales_summary()
            elif user_choice == 5:
                print("Goodbye!")
                break
            else:
                print("Please choose a valid option")
        except ValueError:
            print("Please use a number")

main()
