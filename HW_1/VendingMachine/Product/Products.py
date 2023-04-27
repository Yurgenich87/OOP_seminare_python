class Product:
    """Конструктор продукта с двумя параметрами"""
    def __init__(self, name, price=None):
        self.name = name
        self.price = price

    def get_name(self):
        """Возвращает имя продукта"""
        return self.name

    def set_name(self, value):
        """Устанавливает имя продукта"""
        self.value = value

    def get_price(self):
        """Возвращает цену продукта"""
        return self.price

    def set_price(self, value):
        """Устанавливает цену продукта"""
        if value <= 0:
            raise ValueError("Цена указана некорректно!")
        self.price = value
        return self.to_dict()

    def to_string(self):
        """Возвращает строку, представляющую продукт"""
        return f"name='{self.name}', price={self.price}"

    def to_dict(self):
        """Возвращает словарь с продуктами"""
        prod_dict = {
            "name": self.name,
            "price": self.price,
        }
        return prod_dict


class BottleOfWater(Product):
    """Конструктор бутылки воды с тремя параметрами"""
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def get_volume(self):
        """Возвращает объем бутылки"""
        return self.volume

    def set_volume(self, volume):
        """Устанавливает объем бутылки"""
        self.volume = volume
        return self.to_dict()

    def to_string(self):
        """Возвращает строку, представляющую бутылку воды"""
        return f"name='{super().get_name()}', price={super().get_price()}, volume={self.volume}"

    def to_dict(self):
        """Возвращает словарь с продуктами  в бутылках"""
        prod_dict = super().to_dict()
        prod_dict["volume"] = self.volume
        return prod_dict


class HotDrink(Product):
    """Конструктор горячего напитка с четырьмя параметрами"""
    def __init__(self, name, price, volume, temperature):
        super().__init__(name, price)
        self.volume = volume
        self.temperature = temperature

    def get_temperature(self):
        """Возвращает температуру напитка"""
        return self.temperature

    def set_temperature(self, temperature):
        """Устанавливает температуру напитка"""
        self.temperature = temperature
        return self.to_dict()

    def to_string(self):
        """Возвращает строку, представляющую горячий напиток"""
        return f"name='{super().get_name()}', price={super().get_price()}, volume={self.volume}," \
               f" temperature={self.temperature}"

    def count_name(self):
        """Возвращает количество горячих напитков с одним и тем же именем"""
        number = 0
        number += 1
        return f"{self.name}{number}"

    def to_dict(self):
        """Возвращает словарь с продуктами  в бутылках"""
        prod_dict = super().to_dict()
        prod_dict["volume"] = self.volume
        prod_dict["temperature"] = self.temperature
        return prod_dict
