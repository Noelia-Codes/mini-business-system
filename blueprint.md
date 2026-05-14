📦 Inventory System — Blueprint

🟢 Version 1 (Current Build)

🎯 Goal
A functional inventory system with basic sales tracking.

🧱 Data Structures
inventory = {}
sales_log = []

📦 Inventory Structure
inventory = {
     "shirt": {
     "price": 10.0,
     "stock": 5,
     "sold_quantity": 2,
     "category": "clothing",
     "supplier": "nike"
     }
}

🧾 Sales Log Structure
sales_log = [
     {
     "product": "shirt",
     "quantity": 2,
     "total": 20.0,
     "date": "14/05/2026"
     }
]

🧠 Core Functions (V1)

1. Add Product
     * Input product name (normalized)
     * Check if product exists
        * If yes → ask to update stock
        * If no → create new product
     * Validate inputs:
        * price (float)
        * stock (int)
        * category (text)
        * supplier (text)

2. Sell Product
* Search product in inventory
* If not found → show error message
* If found:
    * Validate quantity
    * Check stock availability
    * If enough stock:
        * Reduce stock
        * Update sold_quantity
        * Calculate total price
        * Create sales record
        * Add automatic date
        * Append to sales_log
    * If not enough stock:
        * Reject sale

3. View Inventory (V1)
* Option A: display all products
* Option B: display a single product by name

4. Sales Summary (V1 Basic)
* Display all sales records
* Print entries from sales_log

5. Menu System

* Loop using while True
* Input validation (integer)
* Route using if/elif

🟡 Version 2 (Future Improvements)

Enhanced View Inventory
* Filter by:
  * category
  * supplier
  * stock level

Smart Search
* Partial name matching
* Optional fuzzy search

Advanced Sales Summary
* Total revenue
* Best-selling product
* Sales per product
* Total units sold

Partial Sales
* Allow selling less stock than requested
* User confirmation required

UX Improvements
* Cancel operations during input
* Better error handling
* Retry loops for invalid input

Data Persistence
* Save inventory to file
* Load inventory on startup

🚀 Summary

Version 1 is complete when:
* Inventory system works
* Selling works
* Sales log works
* View inventory works
* Menu system works

Version 2 focuses on:
* Filters
* Analytics
* Partial sales
* Better UX
* Persistence
