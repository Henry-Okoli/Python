# a welcome note 
print("Welcome to Africa Continental Cafe- \n \nWhat can we serve you")

# menu list 
menu = ["Egusi Soup", "Vegetables Soup", "Rice", "beans", "Garri", "Akpu", "Semo", "Sarad"]

# stock dictionary 
stock = {
    "Egusi Soup": 3, 
    "Vegetables Soup": 23,
    "Rice":5,
    "beans" :7,
    "Garri": 9,
    "Akpu": 8,
    "Semo":2,
    "Sarad": 8
}

# price of each menu
price = {
    "Egusi Soup": 4.1, 
    "Vegetables Soup": 2.3,
    "Rice":1.3,
    "beans" :2.4,
    "Garri": 1.9,
    "Akpu": 3.2,
    "Semo":2.7,
    "Sarad": 8.1
}
# list the iteams and their prices 
print("Menu:")
for items in menu:
    stack_quantity = stock.get(items,0)
    stock_price = price.get(items,0.0)
    print("-", items, "(stock:", stack_quantity, ")", "-", "price: ", stock_price)

# To calculate the total worth of menu in stock
total_stock_Value = 0.0
for items in menu:
    stack_quantity = stock.get(items,0)
    stock_price = price.get(items,0.0)
    total_stock = stack_quantity * stock_price
    total_stock_Value += total_stock 
print ("\nTotal worth of the menu in stock: £ ", total_stock_Value)

print("\nTHANK YOU FOR VISITING OUR CAFE")

