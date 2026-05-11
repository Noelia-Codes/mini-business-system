product_names = set()
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
menu = ["Inventory System:", "1. Add Product", "2. Sell Product", "3. View Inventory", "4. Sales Summary", "5. Exit"]
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
def sell_product():
  
def view_inventory():
  
def sales_summary():
  
def validate_menu_option():
  
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
  
def validate_product_name():
  
def find_product():
  
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
