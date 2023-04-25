

# Создание списка из названий товаров для меню
from HW_1.main import itemMachin

names = [prod.name for prod in itemMachin.get_prod_all()]
names_string = " ".join(names)
print(names_string)