class ShoppingCart:
    def __init__(self):
        self.items = []
        

    def add_item(self, item_name, price):
        item = (item_name,price)
        self.items.append(item)

    def remove_item(self,item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self):
        total = 0
        for item in self.items:
            total = total + item[1]
        print("Total Price :",total)

    def show_products(self):
        print(" -Current Cart- ")
        for products in self.items:
            print(f"Name: {products[0]} Price: {products[1]}")

cart = ShoppingCart()




while True:
    print("""
    ** Process Lists **
      0 -- Exit
      1 -- Add Product
      2 -- Remove Product
      """)
    process = int(input("Enter a process number : "))
    if process == 0:
        print("Log Out")
        break
    elif process == 1:
        prodcut_name = input("Enter a product name: ")
        product_price = int(input("Enter a product price (must be number) : "))
        cart.add_item(prodcut_name,product_price)
        cart.show_products()
        cart.calculate_total()
        
    elif process == 2:
        prodcut_name = input("Enter a product name: ")
        cart.remove_item(prodcut_name)
        cart.show_products()
        cart.calculate_total()
    




