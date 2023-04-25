
class VendingMachine:
    def __init__(self, volume):
        self.volume = volume
        self.products = []
        self.work_log = []

    def add_product(self, prod):
        self.products.append(prod)

    def add_sales(self, line):
        self.work_log.append(line)

    def get_prod_by_name(self, name):
        for prod in self.products:
            if name in prod.get_name():
                return prod
        return None

    def get_prod_all(self):
        return self.products

