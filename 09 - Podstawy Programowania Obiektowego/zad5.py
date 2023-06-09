class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} : {self.price}"



class Shop:
        def __init__(self, items):
            self.items = items

        def show_items(self):
            for item in self.items:
                print(item)

        def sell_item(self, item_name):
            found = False
            for item in self.items:
                if item.name == item_name:
                    found = True
                    self.items.remove(item)
                    print(f"Sold item: {item}")
            if found == False:
                print("Item not found")

        def try_item(self, item_name):
            found = False
            for item in self.items:
                if item.name == item_name:
                    found = True
                    print('Looks good! ')
                    break
            if found == False:
                print("Item not found")

        def return_item(self, item_name):
            self.items.append(item_name)

        def add_to_shop(self, item):
            self.items.append(item)


shop = Shop([])
shop.add_to_shop(Product('Panties', 59.99))
shop.add_to_shop(Product('T-shirt', 9.99))
shop.add_to_shop(Product('Sweather', 29.99))

print('*******************************')
shop.show_items()
print('*********SELL T_SHIRT****************')
shop.sell_item('T-shirt')
# shop.show_items()


print('*********TRY T_SHIRT****************')
shop.try_item('T-shirt')
print('*********TRY Panties****************')
shop.try_item('Panties')
print('*********RETURN T_SHIRT****************')
shop.return_item(Product('T-shirt', 9.99))