from HW_1.VendingMachine.Product.Products import Product, BottleOfWater, HotDrink
from HW_1.VendingMachine.VandingMashine import VendingMachine

# Создание VendingMachine с нужным количеством продуктов
itemMachin = VendingMachine(300)

# Создание новых продуктов
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

# Печать списка всех товаров
for prod in itemMachin.get_prod_all():
    print(prod.to_string())

# Создание переменной из списка названий товаров для меню
names = [prod.name for prod in itemMachin.get_prod_all()]
names_string = " ".join(names)
