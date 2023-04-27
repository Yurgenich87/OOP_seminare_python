
class VendingMachine:
    def __init__(self, volume):
        self.volume = volume
        self.products = []
        self.work_log = []

    def add_product(self, prod):
        """Добавление нового продукта"""
        self.products.append(prod)

    def add_sales(self, line):
        """Добавление скидок"""
        self.work_log.append(line)

    def get_prod_by_name(self, name):
        """Вывод продукта по имени"""
        for prod in self.products:
            if name in prod.get_name():
                return prod
        return None

    def get_prod_all(self):
        """Вывод всех продуктов"""
        return self.products

