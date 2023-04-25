import json

from HW_1.Product.Products import Product, BottleOfWater, HotDrink
from HW_1.Product.VandingMashine import VendingMachine

# item1 = Product("Cola", 88.0)
# item1.set_price(98.0)
# itemMachin.add_product(item1)

itemMachin = VendingMachine(300)
itemMachin.add_product(Product("chips", 60))
itemMachin.add_product(Product("butter", 50))
itemMachin.add_product(Product("bred", 40))
itemMachin.add_product(Product("snack ", 20))
itemMachin.add_product(BottleOfWater("cola", 88, 500))
itemMachin.add_product(BottleOfWater("water", 188, 1500))
itemMachin.add_product(HotDrink("cofe", 78, 250, 60))
itemMachin.add_product(HotDrink("espresso", 90, 250, 60))
itemMachin.add_product(HotDrink("hot_chocolate", 144, 250, 60))
itemMachin.add_product(HotDrink("cocoa", 110, 250, 70))
itemMachin.add_product(HotDrink("Чай", 58, 200, 80))

# # Печать списка всех товаров
# for prod in itemMachin.get_prod_all():
#     print(prod.to_string())

# Создание переменной из списка названий товаров для меню
names = [prod.name for prod in itemMachin.get_prod_all()]
names_string = " ".join(names)
# print(names[2])

# hot_drink = VendingMachine(volume=1)
# hot_drink_dict = hot_drink.get_prod_all()
# print(f"Вывод:{hot_drink_dict}")
# hot_drink = HotDrink(
# hot_drink_dict = hot_drink.to_dict()
# print(json.dumps(hot_drink_dict, indent=4))
# prod_dicts = []
# for prod in itemMachin.get_prod_all():
#     prod_dict = prod.to_dict()
#     prod_dicts.append(prod_dict)
#     print(prod_dict)
# chips = {"name": "chips", "price": 60}
# butter = {"name": "butter", "price": 50}
# bred = {"name": "bred", "price": 40}
# snack = {"name": "snack", "price": 20}
# cola = {"name": "cola", "price": 88, "volume": 500}
# water = {"name": "water", "price": 188, "volume": 1500}
# coffee = {"name": "coffee", "price": 78, "volume": 250, "temperature": 60}
# espresso = {"name": "espresso", "price": 90, "volume": 250, "temperature": 60}
# hot_chocolate = {"name": "hot_chocolate", "price": 144, "volume": 250, "temperature": 60}
# cocoa = {"name": "cocoa", "price": 110, "volume": 250, "temperature": 70}
# tea = {"name": "tea", "price": 58, "volume": 200, "temperature": 80}


# price =
# volume =
# temperature =










