📦 Mini Business System — Blueprint

🎯 Project Goal

A simple Python-based business management system that simulates product inventory, sales tracking, and basic analytics.
The system is designed to practice:
  * data structures (dictionaries, sets)
  * control flow
  * functions and modular design
  * input validation
  * basic business logic

🧱 Core Features (User Functions)

1. Add Product
  * Add a new product to the system
      * If product already exists:
          * ask user to update stock or cancel
      * If new product:
          * collect all required data


2. Sell Product
  * Search product by name (normalized)
      * If product does not exist:
          * inform user and suggest adding it
      * If product exists:
          * request quantity
          * validate stock availability
          * allow partial sale if stock is insufficient (user confirmation required)
          * update stock and sold quantity

3. View Inventory
  * Display products in a **table format**
  * Default view:
      * product name
      * price
      * stock
  * Optional detailed view:
      * supplier
      * category
      * sold quantity


4. Sales Summary
Provides analytics in three modes:
  * Full ranking:
    * all products included (even zero sales)
    * sorted by selected metric

  * Unsold products
    * products with sold_quantity = 0

  * Top N products
    * user-defined limit

Ranking options:
  * by units sold
  * by revenue (price × sold_quantity)


🧠 Data Model

Products dictionary structure:
Each product is stored as:
  * name (key, normalized)
  * price
  * stock
  * sold_quantity
  * supplier
  * category

Supporting data structure:
  * `products` → dictionary of dictionaries
  * `product_names` → set for uniqueness control


🛡️ Validation Rules
  * All product names are normalized using:
    * `lower()`
    * `strip()`

* Menu input must be valid (strict mode)

* Numeric inputs must be:
    * valid numbers
    * non-negative

* Stock cannot go below zero

* Sales cannot exceed available stock (partial sale allowed only with confirmation)


🔁 Program Flow
1. `main()` starts the system
2. Menu is displayed
3. User selects an option
4. Corresponding function is executed
5. System returns to menu loop
6. Exit ends the program


⚙️ Function Structure
Core functions:
  * add_product()
  * sell_product()
  * view_inventory()
  * sales_summary()

Helper functions:
  * validate_menu_option()
  * validate_number()
  * validate_product_name()
  * find_product()

📊 Design Principles
  * Separation of concerns (each function has one responsibility)
  * Strict input validation
  * Clean data normalization
  * Structured business logic
  * Scalable design (future database or CSV migration ready)
