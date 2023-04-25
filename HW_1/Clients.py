class Client:
    """Конструктор Клиента с двумя параметрами"""
    def __init__(self, name, buy=None):
        self.name = name
        self.buy = buy

    def get_name(self):
        # Возвращает имя продукта
        return self.name

    def set_name(self, value):
        # Устанавливает имя продукта
        self.value = value

    def buy(self):
        # Возвращает цену продукта
        return self.price

    def set_buy(self, value):
        # Устанавливает цену продукта
        if value <= 0:
            raise ValueError("Цена указана некорректно!")
        self.buy = value

    def to_string(self):
        # Возвращает строку, представляющую продукт
        return f"name='{self.name}', price={self.buy}"

class Client:
    """Конструктор Клиента с двумя параметрами"""
    def __init__(self, name, price=None):
        self.name = name
        self.buy = price